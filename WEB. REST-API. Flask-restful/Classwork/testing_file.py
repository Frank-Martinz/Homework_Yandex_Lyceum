import requests
from pprint import pprint

# Получение пользователя (Корректно)
pprint(requests.get('http://127.0.0.1:5000/api/v2/users/1').json())

# Получение пользователя (Некорректно. пользователя с id 6 нет)
pprint(requests.get('http://127.0.0.1:5000/api/v2/users/6').json())

# Добавление пользователя (Корректно)
pprint(requests.post('http://127.0.0.1:5000/api/v2/users', json={'name': 'Dmitrii',
                                                                 'surname': 'Andrianov',
                                                                 'age': 15,
                                                                 'speciality': 'Programmer',
                                                                 'position': 'Programmer',
                                                                 'address': 'module_1',
                                                                 'city_from': 'Vladivostok',
                                                                 'email': 'andrianovdmitrii2007@gmail.com',
                                                                 'password': 'Digo381323'}).json())

# Добавление пользователя (Некорректно. Переданы не все аргументы или в неправильном формате)
pprint(requests.post('http://127.0.0.1:5000/api/v2/users', json={'name': 'Dmitrii',
                                                                 'surname': 'Andrianov',
                                                                 'age': 'here have to be integer',
                                                                 'city_from': 'Vladivostok'}).json())

# Изменение пользователя (Корректно)
pprint(requests.put('http://127.0.0.1:5000/api/v2/users/5', json={'name': 'Дмитрий'}).json())

# Изменение пользователя (Некорректно. Передан id, которого нет)
pprint(requests.put('http://127.0.0.1:5000/api/v2/users/6', json={'name': 'Дмитрий'}).json())

# Удаление пользователя (Корректно)
pprint(requests.delete('http://127.0.0.1:5000/api/v2/users/5').json())

# Удаление пользователя (Некорректно)
pprint(requests.delete('http://127.0.0.1:5000/api/v2/users/6').json())
