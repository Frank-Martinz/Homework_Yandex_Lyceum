from flask import Flask, url_for, request, render_template, redirect
import random
import json

# После запуска программы переходим по ссылке: http://127.0.0.1:8080/member
# После каждого обновления страницы будет появляться информация о разных членах команды

app = Flask(__name__)


@app.route('/member')
def mars_galary():
    with open('templates/team.json', encoding='utf8') as file:
        f = file.read()
        data = json.loads(f)
        data = data['team'][random.randint(0, 5)]

    return render_template('members.html', name=data['name'], age=data['age'], prof=data['prof'])


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(port=8080, host='127.0.0.1')
