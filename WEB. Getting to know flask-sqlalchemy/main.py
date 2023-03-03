from flask import Flask, url_for, request, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs

# После запуска программы переходим по ссылке: http://127.0.0.1:5000/ где и будет лежать ответ

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    app.run()


@app.route('/')
@app.route('/answer')
def tablet():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs)
    return render_template('tablets.html', job=job)


if __name__ == '__main__':
    main()
