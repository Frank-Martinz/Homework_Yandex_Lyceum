import flask
from flask import request
from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    user = db_sess.query(User).all()
    return flask.jsonify(
        {
            'user': [item.to_dict(only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'city_from'))
                     for item in user]
        }
    )


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_one_job(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return flask.jsonify({'Error': '400 not found'})
    return flask.jsonify(
        {
            'user': user.to_dict(only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'city_from'))
        }
    )


@blueprint.route('/api/users', methods=['POST'])
def create_job():
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['surname', 'name', 'age', 'position', 'speciality', 'address', 'city_from']):
        return flask.jsonify({'error': 'Bad request'})

    db_sess = db_session.create_session()
    user = User(
        surname=request.json['surname'],
        name=request.json['name'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        city_from=request.json['city_from']
    )
    db_sess.add(user)
    db_sess.commit()
    return flask.jsonify({'Status': 'Ok'})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_job(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).get(user_id)
    if not user:
        return flask.jsonify({'error': 'Not found'})
    db_sess.delete(user)
    db_sess.commit()
    return flask.jsonify({'Status': 'Ok'})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_job(user_id):
    if not request.json:
        return flask.jsonify({'error': 'Empty request'})

    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()

    if not user:
        return flask.jsonify({'Error': '404 Not found'})

    changing_values = {
        'name': user.name,
        'surname': user.surname,
        'age': user.age,
        'position': user.position,
        'speciality': user.speciality,
        'address': user.address,
        'city_from': user.city_from
    }
    for item in request.json:
        if item in changing_values:
            changing_values[item] = request.json[item]

    user.name = changing_values['name']
    user.surname = changing_values['surname']
    user.age = changing_values['age']
    user.position = changing_values['position']
    user.speciality = changing_values['speciality']
    user.address = changing_values['address']
    user.city_from = changing_values['city_from']

    db_sess.commit()
    return flask.jsonify({'Status': 'Ok'})
