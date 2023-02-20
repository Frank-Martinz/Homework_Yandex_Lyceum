from flask import Flask, url_for, request, render_template, redirect

# После запуска программы переходим по ссылке: http://127.0.0.1:8080/galery Там будет лежать решение

app = Flask(__name__)

FILES = ['/static/photo_from_mars1.jpg', '/static/photo_from_mars2.png', '/static/photo_from_mars3.png']


@app.route('/galery', methods=['POST', 'GET'])
def mars_galary():
    if request.method == 'POST':
        name, f = request.files['file'].filename, request.files['file']
        with open(f'static/{name}', 'wb') as file:
            file.write(f.read())
        FILES.append(f'/static/{name}')

    return render_template('carousel.html', files=FILES)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.run(port=8080, host='127.0.0.1')
