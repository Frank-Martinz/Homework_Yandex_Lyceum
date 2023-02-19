from flask import Flask, url_for, request, render_template, redirect

# После запуска программы нужно перейти по ссылке: http://127.0.0.1:8080/table/<sex>/<age>
# (sex: female/male, age: 1-89)

app = Flask(__name__)


@app.route('/table/<sex>/<age>')
def making_cabin(sex, age):
    return render_template('cabin.html', sex=sex, age=int(age))


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(port=8080, host='127.0.0.1')
