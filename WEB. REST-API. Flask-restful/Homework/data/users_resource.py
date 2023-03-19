import flask
from flask import request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from . import db_session
from .users import User

parser = reqparse.RequestParser()
parser.add_argument('surname')
parser.add_argument('name')
parser.add_argument('age', type=int)
parser.add_argument('position')
parser.add_argument('speciality')
parser.add_argument('address')
parser.add_argument('city_from')
parser.add_argument('password')
parser.add_argument('email')


def abort_if_jobs_not_found(users_id):
    session = db_session.create_session()
    user = session.query(User).get(users_id)
    if not user:
        abort(404, message=f"User {users_id} not found")


class UserResource(Resource):
    def get(self, users_id):
        abort_if_jobs_not_found(users_id)
        session = db_session.create_session()
        user = session.query(User).get(users_id)
        return jsonify({'user': user.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'city_from'))})

    def delete(self, users_id):
        abort_if_jobs_not_found(users_id)
        session = db_session.create_session()
        user = session.query(User).get(users_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def put(self, users_id):
        abort_if_jobs_not_found(users_id)
        args = parser.parse_args()
        session = db_session.create_session()
        user = session.query(User).get(users_id)

        user.surname = args['surname'] if not args['surname'] is None else user.surname
        user.name = args['name'] if not args['name'] is None else user.name
        user.age = args['age'] if not args['age'] is None else user.age
        user.position = args['position'] if not args['position'] is None else user.position
        user.speciality = args['speciality'] if not args['speciality'] is None else user.speciality
        user.city_from = args['city_from'] if not args['city_from'] is None else user.city_from
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address', 'city_from')) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        if not all(args.values()):
            return jsonify({'Error': 'Any or all arguments were not given'})
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            city_from=args['city_from']
        )
        user.email = args['email']
        user.set_password(args['password'])
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
