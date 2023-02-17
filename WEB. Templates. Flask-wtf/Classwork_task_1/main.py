from flask import Flask, url_for, request, render_template

# После запуска приложения по ссылке: http://127.0.0.1:8080/<title> или http://127.0.0.1:8080/index/<title>
# будет находится решение задачи

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=f'{title}')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
