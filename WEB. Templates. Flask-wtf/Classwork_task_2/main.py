from flask import Flask, url_for, request, render_template

# После запуска приложения по ссылке: http://127.0.0.1:8080/training/<prof> (prof - профессия) будет лежать решение

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    if prof.lower() in ['инженер', 'изобретатель', 'маркшейдер', 'программист', 'разработчик']:
        prof = 1
    else:
        prof = 0
    image_url = str(url_for("static", filename=f"plan_of_starship_{prof}.jpg"))
    return render_template('base.html', profession=prof, images_url=image_url)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
