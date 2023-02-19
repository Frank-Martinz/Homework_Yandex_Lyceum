from flask import Flask, url_for, request, render_template, redirect

# После запуска программы перейдите по ссылке: http://127.0.0.1:8080/form_sample и заполните форму
# После того, как вы нажмёте кнопку "Записаться", вы перейдёте на ссылку http://127.0.0.1:8080/auto_answer
# где будет информация, которую вы только что заполнили

app = Flask(__name__)

information = dict()


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    global information
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='for_form.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <div class="text-box">
                                <h1 class="text-mod">Анкета претендента</h1>
                                <h2 class="text-mod">на участие в миссии</h2>
                            </div>
                            <div class="block1">
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    </br class="indent">
                                    <input type="email" class="form-control" id="email"aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    </br class="indent">
                                    <div class="form-control">
                                        <label for="educationSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="type">
                                            <option>Дошкольное</option>
                                            <option>Начальное</option>
                                            <option>Основное Среднее</option>
                                            <option>Среднее общее</option>
                                            <option>Среднее профессиональное</option>
                                            <option>Высшее образование</option>
                                        </select>
                                     </div>
                                    </br class="indent">
                                    <div class="form-group">
                                        <label for="profession">Какие у вас есть профессии?</label>
                                        </br>
                                        <input type="checkbox" id="research_engineer" name="research_engineer">
                                        <label for="research_engineer">Инженер-исследователь</label>
                                        </br>
                                        <input type="checkbox" id="pilot" name="pilot">
                                        <label for="pilot">Пилот</label>
                                        </br>
                                        <input type="checkbox" id="builder" name="builder">
                                        <label for="builder">Строитель</label>
                                        </br>
                                        <input type="checkbox" id="exobiologist" name="exobiologist">
                                        <label for="exobiologist">Экзобиолог</label>
                                        </br>
                                        <input type="checkbox" id="astrogeologist" name="astrogeologist">
                                        <label for="astrogeologist">Астрогеолог</label>
                                        </br>
                                        <input type="checkbox" id="meteorologist" name="meteorologist">
                                        <label for="meteorologist">Метеоролог</label>
                                        </br>
                                        <input type="checkbox" id="doctor" name="doctor">
                                        <label for="doctor">Врач</label>
                                    </div>
                                    </br class="indent">
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    </br class="indent">
                                     <div class="form-group">
                                        <label for="why">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="why" rows="3" name="why"></textarea>
                                    </div>
                                    </br class="indent">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    </br class="indent"> 
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                    </div>
                                    </br class="indent">
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        if 'accept' in request.form:
            ready = request.form['accept']
        else:
            ready = ''
        prof = list()
        if list(request.form.keys())[4] != 'sex':
            for item in list(request.form.keys())[4:]:
                if item == 'sex':
                    break
                else:
                    prof.append(item)
        else:
            prof = ['Нет профессий']
        information = {'surname': request.form['surname'],
                       'name': request.form['name'],
                       'educ': request.form['type'],
                       'sex': request.form['sex'],
                       'motiv': request.form['why'],
                       'ready': ready,
                       'prof': ', '.join(prof)}
        return redirect(url_for(f'auto_answer'), 301)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html', info=information)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
