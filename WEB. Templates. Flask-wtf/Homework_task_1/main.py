from flask import Flask, url_for, request, render_template, redirect

# После запуска программы нужно перейти по ссылке: http://127.0.0.1:8080/distribution где будет лежать ответ

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    team = ['Ридли Скотт', 'Эндри Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', team=team)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(port=8080, host='127.0.0.1')
