import flask
from flask import request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from . import db_session
from .jobs import Jobs

parser = reqparse.RequestParser()
parser.add_argument('job')
parser.add_argument('team_leader', type=int)
parser.add_argument('work_size', type=int)
parser.add_argument('collaborators')
parser.add_argument('is_finished', type=bool)


def abort_if_jobs_not_found(jobs_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(jobs_id)
    if not job:
        abort(404, message=f"Job {jobs_id} not found")


class JobResource(Resource):
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(jobs_id)
        return jsonify({'job': job.to_dict(only=('job', 'work_size', 'user.name', 'collaborators', 'is_finished'))})

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(jobs_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        args = parser.parse_args()
        session = db_session.create_session()
        job = session.query(Jobs).get(jobs_id)

        job.job = args['job'] if not args['job'] is None else job.job
        job.team_leader = args['team_leader'] if not args['team_leader'] is None else job.team_leader
        job.work_size = args['work_size'] if not args['work_size'] is None else job.work_size
        job.collaborators = args['collaborators'] if not args['collaborators'] is None else job.collaborators
        job.is_finished = args['is_finished'] if not args['is_finished'] is None else job.is_finished
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('job', 'work_size', 'user.name', 'collaborators', 'is_finished')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        if not all([True if not (i is None) else False for i in args.values()]):
            return jsonify({'Error': 'Any or all arguments were not given'})
        job = Jobs(
            job=args['job'],
            team_leader=args['team_leader'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
