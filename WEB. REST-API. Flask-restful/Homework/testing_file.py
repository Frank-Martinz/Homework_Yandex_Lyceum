import requests
from pprint import pprint

# Получение работы (Корректно)
pprint(requests.get('http://127.0.0.1:5000/api/v2/jobs/1').json())

# Получение работы (Некорректно. пользователя с id 6 нет)
pprint(requests.get('http://127.0.0.1:5000/api/v2/jobs/6').json())

# Добавление работы (Корректно)
pprint(requests.post('http://127.0.0.1:5000/api/v2/jobs', json={'job': 'Solve the task',
                                                                'team_leader': 1,
                                                                'work_size': 4,
                                                                'collaborators': '2, 3',
                                                                'is_finished': False}).json())

# Добавление работы(Некорректно. Переданы не все аргументы или в неправильном формате)
pprint(requests.post('http://127.0.0.1:5000/api/v2/jobs', json={'job': 'Solve the task',
                                                                'team_leader': 1,
                                                                'collaborators': '2, 3',
                                                                'is_finished': 'False'}).json())

# Изменение работы (Корректно)
pprint(requests.put('http://127.0.0.1:5000/api/v2/jobs/4', json={'team_leader': 2}).json())

# Изменение работы (Некорректно. Передан id, которого нет)
pprint(requests.put('http://127.0.0.1:5000/api/v2/jobs/6', json={'team_leader': 2}).json())

# Удаление работы (Корректно)
pprint(requests.delete('http://127.0.0.1:5000/api/v2/jobs/4').json())

# Удаление работы (Некорректно)
pprint(requests.delete('http://127.0.0.1:5000/api/v2/jobs/4').json())
