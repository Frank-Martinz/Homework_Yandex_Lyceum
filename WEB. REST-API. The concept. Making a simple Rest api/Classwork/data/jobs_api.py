import flask
from flask import request
from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return flask.jsonify(
        {
            'jobs': [item.to_dict(only=('job', 'work_size', 'user.name', 'collaborators', 'is_finished')) for item in
                     jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return flask.jsonify({'Error': '400 not found'})
    return flask.jsonify(
        {
            'job': job.to_dict(only=('job', 'work_size', 'user.name', 'collaborators', 'is_finished'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return flask.jsonify({'error': 'Bad request'})

    db_sess = db_session.create_session()
    any_same = db_sess.query(Jobs).filter(Jobs.id == request.json['id']).first()
    if not (any_same is None):
        return flask.jsonify({'error': 'Id already exists'})
    job = Jobs(
        id=request.json['id'],
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(job)
    db_sess.commit()
    return flask.jsonify({'Status': 'Ok'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_job(jobs_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(jobs_id)
    if not jobs:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(jobs)
    db_sess.commit()
    return flask.jsonify({'Status': 'Ok'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def edit_job(jobs_id):
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})

    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == jobs_id).first()

    if not jobs:
        return flask.jsonify({'Error': '404 Not found'})

    changing_values = {
        'team_leader': jobs.team_leader,
        'job': jobs.job,
        'work_size': jobs.work_size,
        'collaborators': jobs.collaborators,
        'is_finished': jobs.is_finished
    }
    for item in request.json:
        if item in changing_values:
            changing_values[item] = request.json[item]

    for item in request.json:
        jobs.team_leader = changing_values['team_leader']
        jobs.job = changing_values['job']
        jobs.work_size = changing_values['work_size']
        jobs.collaborators = changing_values['collaborators']
        jobs.is_finished = changing_values['is_finished']

    db_sess.commit()
    return flask.jsonify({'Status': 'Ok'})
