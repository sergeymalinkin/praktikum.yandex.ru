# Запросите погодный сервис http://wttr.in по URL без параметров.
# А их задайте словарём weather_parameters.
# Функция get() должна принимать его, как отдельный аргумент params.

import requests

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    'T': '',  # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
    'M': '',
    'lang': 'ru'

}

response = requests.get(url, params=weather_parameters)

print(response.text)
