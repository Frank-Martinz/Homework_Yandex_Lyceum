from flask import Flask, url_for, request, render_template, redirect, abort
from data import db_session
from data.users import User
from data.jobs import Jobs
from forms.user import RegisterForm
from forms.login import LoginForm
from forms.jobsform import JobsForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

db_session.global_init('db/blogs.db')


def main():
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
            email=form.login.data
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
        job = db_sess.query(Jobs).filter(Jobs.id == id,
                                         Jobs.user == current_user).first()
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
    jobs = db_sess.query(Jobs).filter(Jobs.id == id,
                                      Jobs.user == current_user
                                      ).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/tables')


if __name__ == '__main__':
    main()
