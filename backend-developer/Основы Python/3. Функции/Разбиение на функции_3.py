# Добавьте в функцию process_query() обработку ещё одного запроса 'Кто все мои друзья?'.
# В ответ нужно выводить на экран Твои друзья: {список_друзей}, где {список_друзей} — строка,
# состоящая из списка друзей, разделённых запятой и пробелом.
# Добавьте вызов process_query('Кто все мои друзья?') в тело основной программы.

FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']


def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')


def process_query(query):
    print("Привет, я Анфиса!")
    count = len(FRIENDS)
    if query == 'Сколько у меня друзей?':
        print_friends_count(count)
    elif query == 'Кто все мои друзья?':
        print("Твои друзья: " + "" + ", ".join(FRIENDS))
    else:
        print('<неизвестный запрос>')


process_query('Сколько у меня друзей?')
process_query('Как меня зовут?')
process_query('Кто все мои друзья?')