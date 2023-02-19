from flask import Flask, url_for, request, render_template

# После запуска приложения по ссылке: http://127.0.0.1:8080/list_prof/<type_printing> (type_printing - то, как будут выводиться профессии:
# ul - нумерация, ol - без нумерации) будет лежать решение

app = Flask(__name__)


@app.route('/list_prof/<type_printing>')
def news(type_printing):
    profession_list = ['Инженер-исследователь', 'Пилот', 'Строитель', 'экзобиолог', 'Врач',
                       'Инженер по терраформированию', 'Климатолог', 'Специалист по радиационной защите',
                       'астрогеолог', 'Гляциолог', 'Инженер жизнеобеспечения', 'Метеоролог', 'Оператор марсохода',
                       'Киберинженер', 'Штурман', 'Пилот дронов']
    return render_template('base.html', prof_list=profession_list, print_type=type_printing)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
