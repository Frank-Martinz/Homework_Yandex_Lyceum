from flask import Flask, request, render_template, redirect, abort, make_response, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from forms.user import RegisterForm
from forms.login import LoginForm
from forms.jobsform import JobsForm
from forms.departmentsform import DepartmentsForm
from data import users_resource
from data import jobs_resource
import requests
from PIL import Image
import base64
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)

login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init('db/blogs.db')

api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UserResource, '/api/v2/users/<int:users_id>')
api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
api.add_resource(jobs_resource.JobResource, '/api/v2/jobs/<int:jobs_id>')


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_session.global_init('db/blogs.db')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.login.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.position.data,
            address=form.address.data,
            email=form.login.data,
            city_from=form.city_from.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/tables", code=302)
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route('/tables', methods=['GET', 'POST'])
def tables():
    form = JobsForm()
    if form.validate_on_submit():
        return redirect('/add_jobs')
    else:
        if current_user.is_authenticated:
            db_sess = db_session.create_session()
            jobs = db_sess.query(Jobs).filter()
            return render_template('tablets.html', job=jobs)
        else:
            return redirect('/login')


@app.route('/add_jobs', methods=['GET', 'POST'])
def add_job():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        print(form.collaborators.data)
        job = Jobs(
            job=form.job.data,
            team_leader=form.team_lead.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/tables', code=302)

    else:
        if current_user.is_authenticated:
            return render_template('add_jobs.html', form=form, title='Добавление работ')
        else:
            return redirect('/login')


@app.route('/edit_jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = JobsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id, Jobs.user == current_user).first()
        if job is None:
            job = db_sess.query(Jobs).filter(Jobs.id == id, current_user.id == 1).first()

        if job:
            form.job.data = job.job
            form.team_lead.data = job.team_leader
            form.collaborators.data = job.collaborators
            form.work_size.data = job.work_size
            form.is_finished.data = job.is_finished
        else:
            abort(404)

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                          Jobs.user == current_user).first()
        if jobs is None:
            jobs = db_sess.query(Jobs).filter(Jobs.id == id, current_user.id == 1).first()

        if jobs:
            jobs.job = form.job.data
            jobs.team_lead = form.team_lead.data
            jobs.collaborators = form.collaborators.data
            jobs.work_size = form.work_size.data
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/tables')
        else:
            abort(404)

    else:
        if current_user.is_authenticated:
            return render_template('add_jobs.html', form=form, title='Редактирование работ')
        return redirect('/login')


@app.route('/delete_jobs/<int:id>')
@login_required
def delete_jobs(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id, Jobs.user == current_user).first()
    if job is None:
        job = db_sess.query(Jobs).filter(Jobs.id == id, current_user.id == 1).first()

    if job:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/tables')


@app.route('/departments')
@login_required
def departments():
    form = DepartmentsForm()
    if form.validate_on_submit():
        return redirect('/add_department')
    else:
        if current_user.is_authenticated:
            db_sess = db_session.create_session()
            depart = db_sess.query(Department).filter()
            return render_template('departments_tab.html', department=depart)
        else:
            return redirect('/login')


@app.route('/add_department', methods=['GET', 'POST'])
@login_required
def add_department():
    form = DepartmentsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()

        depart = Department(
            title=form.title.data,
            chief=form.chief.data,
            members=form.members.data,
            email=form.email.data,
        )
        db_sess.add(depart)
        db_sess.commit()
        return redirect('/departments', code=302)

    else:
        if current_user.is_authenticated:
            return render_template('add_department.html', form=form, title='Добавление департамента')
        else:
            return redirect('/login')


@app.route('/edit_depart/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    form = DepartmentsForm()
    if request.method == 'GET':
        db_sess = db_session.create_session()
        depart = db_sess.query(Department).filter(Department.id == id, Department.user == current_user).first()
        if depart is None:
            depart = db_sess.query(Department).filter(Department.id == id, current_user.id == 1).first()

        if depart:
            form.title.data = depart.title
            form.chief.data = depart.chief
            form.members.data = depart.members
            form.email.data = depart.email

        else:
            abort(404)

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        depart = db_sess.query(Department).filter(Department.id == id,
                                                  Department.user == current_user).first()
        if depart is None:
            depart = db_sess.query(Department).filter(Department.id == id, current_user.id == 1).first()

        if depart:
            depart.title = form.title.data
            depart.chief = form.chief.data
            depart.members = form.members.data
            depart.email = form.email.data
            db_sess.commit()
            return redirect('/departments')
        else:
            abort(404)

    else:
        if current_user.is_authenticated:
            return render_template('add_department.html', form=form, title='Редактирование работ')
        return redirect('/login')


@app.route('/delete_depart/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    db_sess = db_session.create_session()
    depart = db_sess.query(Department).filter(Department.id == id, Department.user == current_user).first()
    if depart is None:
        depart = db_sess.query(Department).filter(Department.id == id, current_user.id == 1).first()

    if depart:
        db_sess.delete(depart)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments')


@app.route('/users_show/<int:user_id>')
def show_city(user_id):
    info = requests.get(f'http://127.0.0.1:5000/api/users/{user_id}').json()
    if 'Error' in info or 'error' in info:
        abort(404)
        return

    city = info['user']['city_from']
    api_server = 'https://geocode-maps.yandex.ru/1.x/'
    geocode_params = {
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'geocode': city,
        'format': 'json'
    }
    data = requests.get(api_server, params=geocode_params).json()
    if not data or 'statusCode' in data:
        abort(404)
        return
    coords = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')

    api_server = 'http://static-maps.yandex.ru/1.x/'
    params = {
        'll': f'{coords[0]},{coords[1]}',
        'l': 'sat',
        'z': 10,
        'size': '600,450'
    }
    data = requests.get(api_server, params=params)
    if not data:
        abort(404)
        return

    with open('static/city_image.jpeg', 'wb') as file:
        file.write(data.content)

    im = Image.open("static/city_image.jpeg")
    data = io.BytesIO()
    im.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())

    return render_template('show_users_city.html', img_data=encoded_img_data.decode('utf-8'),
                           user_name=f'{info["user"]["surname"]}{info["user"]["name"]}',
                           city=city)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404 Not found'})), 404


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'Error': '400 Bad request'})), 404


if __name__ == '__main__':
    main()
