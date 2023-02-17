from flask import Flask, url_for, request, redirect

app = Flask(__name__)


# После запуска программы переходим по ссылке: http://127.0.0.1:8080/carousel


@app.route('/')
def start_wind():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    prom = ['Человечество вырастает из детства.', '',
            'Человечеству мала одна планета.', '',
            'Мы сделаем обитаемыми безжизненные пока планеты.', '',
            'И начнем с Марса!', '',
            'Присоединяйся!']
    return '</br>'.join(prom)


@app.route('/image_mars')
def image_mars():
    html_request = f'''<!doctype html>
        <html lang="ru">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Демо Bootstrap</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
            <link href="{url_for('static', filename='image_mars.css')}" rel="stylesheet" type="text/css">
          </head>
          <body>
            <header>Жди нас, Марс!</header>
            <img src="{url_for("static", filename="mars.png")}" alt="здесь должна была быть картинка, но не нашлась">
            <div class="p-3 bg-dark-subtle text-dark border border-dark-border-subtle rounded-3">Человечество вырастает из детства.</div>
            <div class="p-3 bg-success-subtle text-success border border-success-border-subtle rounded-3">Человечеству мала одна планета.</div>
            <div class="p-3 bg-secondary-subtle text-secondary border border-secondary-border-subtle rounded-3">Мы сделаем обитаемыми безжизненные пока планеты.</div>
            <div class="p-3 bg-warning-subtle text-warning border border-warning-border-subtle rounded-3">И начнем с Марса!</div>
            <div class="p-3 bg-danger-subtle text-danger border border-danger-border-subtle rounded-3">Присоединяйся!</div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
          </body>
        </html>'''
    return html_request


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
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
        '''print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])'''
        print(request.form)
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice_of_planet(planet_name):
    planets_name = {
        'Меркурий': ['Меркурий', 'Самая близкая планета к Солнцу', 'На ней тепло',
                     '58 земных дней = 1 день на Меркурии', 'На ней, как на курорте', 'Маленькая и уютная)'],
        'Венера': ['Венеру', 'Вторая планета по удаленности от Солнца', '1 год > 1 дня (Успеешь сделать всё)',
                   'Близко к земле', 'Нет спутников => Есть шанс стать вторым Илоном Маском',
                   'Обладает плотной атмосферой'],
        'Земля': ['Землю', 'Родная наша планета', 'Никуда не надо лететь', 'Шикарная атмосфера',
                  'Прекрасная погода и температура', 'Свежий воздух :)'],
        'Марс': ['Марс', 'Четвёртая планета по удалённости от Солнца', 'На ней много необходимых ресурсов',
                 'На ней есть вода и атмосфера', 'На ней есть небольшое магнитное поле', 'Наконец, она просто красива'],
        'Юпитер': ['Юпитер', 'Пятая планета по удалённости от Солнца', 'Самая большая планета Солнечной системы',
                   'Газовый ГИГАНТ!', 'ОООЧЕНЬ КОРОТКИЕ СУТКИ! ~10 ЧАСОВ!',
                   'Будешь много свободного места для бизнеса'],
        'Сатурн': ['Сатурн', 'Шестая планета по удалённости от Солнца', 'Газовый ГИГАНТ!',
                   'Названо в честь римского бога земледелия', 'Много колечек! (Похож на пончик)',
                   'Большая и Красивая'],
        'Уран': ['Уран', 'Седьмая планета по удалённости от Солнца', 'Большая и тяжёлая',
                 'Первая планета, которую открыли в новом времени', 'Ось вращения лежит как бы "На боку"!',
                 'Самую малость прохладно, но это и хорошо. (Летом будет хорошо)'],
        'Нептун': ['Нептун', 'Восьмая планета по удалённости от Солнца', 'Самая дальняя планета',
                   '1 день там = 16 часов на земле', 'Атмосфера состоит в основном из водорода и гелия',
                   'ЛЕДЯНОЙ ГИГАНТ!!!']
    }
    planet_name = str(planet_name).capitalize()
    if planet_name in planets_name:
        return f'''<html lang="ru">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Полетели с нами на {planets_name[planet_name][0]}!</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
              </head>
              <body>
                <h1>Моё предложение: {planet_name}!</h1>
                <h2>{planets_name[planet_name][1]}</h2>
                <div class="p-3 bg-dark-subtle text-dark border border-dark-border-subtle rounded-3">{planets_name[planet_name][2]}</div>
                <div class="p-3 bg-success-subtle text-success border border-success-border-subtle rounded-3">{planets_name[planet_name][3]}</div>
                <div class="p-3 bg-warning-subtle text-warning border border-warning-border-subtle rounded-3">{planets_name[planet_name][4]}</div>
                <div class="p-3 bg-danger-subtle text-danger border border-danger-border-subtle rounded-3">{planets_name[planet_name][5]}</div>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
              </body>
            </html>'''
    else:
        return f'''
                <html lang="ru">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='for_form.css')}" />
                        <title>Ошибка :(</title>
                    </head>
                    <body>
                        <h6>Error 404</h6>
                        <header class="text-mod bigger-text">:(</header>
                        <p class="text-mod bigger-text">Такой планеты нет в Солнечной системе</p>
                    </body>
                </html>
                '''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def test(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
                    <link href="{url_for('static', filename='image_mars.css')}" rel="stylesheet" type="text/css">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {str(nickname)}:</h2>
                    <div class="p-3 bg-success-subtle text-success rounded-3">Поздравляем! Ваш рейтинг после {str(level)} этапа отбора</div>
                    <div class="p-3 text-dark rounded-3">составляет {str(rating)}!</div>
                    <div class="p-3 bg-warning-subtle text-warning rounded-3">Желаем удачи!</div>
                  </body>
                </html>'''


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'POST':
        f = request.files['file']
        with open('static/image.png', 'wb') as file:
            file.write(f.read())

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
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1 class="text-mod">Загрузка фотографии</h1>
                                <h2 class="text-mod">для участия в миссии</h2>
                                <div class="block2">
                                    <form method="post" enctype="multipart/form-data">
                                       <div class="form-group">
                                            <label for="photo">Выберите файл</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        </br>
                                        <img src="{url_for("static", filename="image.png")}" alt="" class="imag">
                                        </br>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''


@app.route('/carousel')
def images_carousel():
    return f'''<!doctype html>
              <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='for_form.css')}" />
                <title>Отбор астронавтов</title>
              </head>
              <body>
                  <h1 class="text-mod">Пейзажи марса</h1>
                  <div class="block2">
                      <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                          <div class="carousel-inner">
                            <div class="carousel-item active">
                              <img class="d-block w-100 imag2" src="{url_for('static', filename='photo_from_mars.jpg')}" alt="Первый слайд">
                            </div>
                            <div class="carousel-item">
                              <img class="d-block w-100 imag2" src="{url_for('static', filename='photo_from_mars2.png')}" alt="Второй слайд">
                            </div>
                            <div class="carousel-item">
                              <img class="d-block w-100 imag2" src="{url_for('static', filename='photo_from_mars3.png')}" alt="Второй слайд">
                            </div>
                          </div>
                          <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="sr-only">Previous</span>
                          </a>
                          <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                          </a>
                        </div>
                      </div>
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
              </body>
              </html>
        
'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
