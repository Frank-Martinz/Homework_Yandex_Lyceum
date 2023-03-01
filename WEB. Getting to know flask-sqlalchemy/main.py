from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

# После запуска программы ищем в папке db файл blogs.db
# В нём в таблице users будет лежать решение

def main():
    db_session.global_init("db/blogs.db")

    user = User()
    user.name = 'Ridley'
    user.surname = 'Scott'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'

    user1 = User()
    user1.name = 'Vasya'
    user1.surname = 'Petrov'
    user1.age = 44
    user1.position = 'captain helper'
    user1.speciality = 'research engineer'
    user1.address = 'module_2'
    user1.email = 'vasya_petrov@mars.org'

    user2 = User()
    user2.name = 'Oleg'
    user2.surname = 'Tinkov'
    user2.age = 55
    user2.position = 'investor'
    user2.speciality = 'bank_manager'
    user2.address = 'module_1'
    user2.email = 'olega_tinkov@gmail.com'

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.commit()

    app.run()


if __name__ == '__main__':
    main()
