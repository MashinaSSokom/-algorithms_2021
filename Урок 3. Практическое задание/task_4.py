"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
from uuid import uuid4
from hashlib import sha256

cash = {}


def check_url(url):
    if cash.get(url):
        return print(f'Сайт "{url}" присутствует в кэше')
    cash[url] = sha256(uuid4().hex.encode('utf-8')+url.encode('utf-8')).hexdigest()
    return print(f'Добавили сайт "{url}" в кэш!')


check_url("vk.com")
check_url("vk.com")
check_url("youtube.com")
check_url("youtube.com")
print(cash)

