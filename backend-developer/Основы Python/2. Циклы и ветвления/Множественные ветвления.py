# Научите Анфису склонять слово «сообщения» в зависимости от их количества:

for messages_count in range(0, 21):
    if messages_count > 4:
        print('У вас ' + str(messages_count) + ' новых сообщений')
    elif messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас ' + str(messages_count) + ' новое сообщение')
    elif messages_count == 2:
        print('У вас ' + str(messages_count) + ' новых сообщения')
    elif messages_count == 3:
        print('У вас ' + str(messages_count) + ' новых сообщения')
    elif messages_count == 4:
        print('У вас ' + str(messages_count) + ' новых сообщения')
    else:
        print('У вас нет новых сообщений')

# Анфиса умеет здороваться утром и днём, но ей нужно добавить приветствия для ночи и вечера.
# Напишите условную конструкцию, которая выводит уместные сообщения:
# ВРЕМЯ	ТЕКСТ ПРИВЕТСТВИЯ
# до 6	Доброй ночи!
# до 12	Доброе утро!
# до 18	Добрый день!
# до 23	Добрый вечер!
# в остальных случаях -	Доброй ночи!

for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    if current_hour == 6:
        print("Доброе утро!")
    elif current_hour == 7:
        print("Доброе утро!")
    elif current_hour == 8:
        print("Доброе утро!")
    elif current_hour == 9:
        print("Доброе утро!")
    elif current_hour == 10:
        print("Доброе утро!")
    elif current_hour == 11:
        print("Доброе утро!")
    elif current_hour == 12:
        print("Добрый день!")
    elif current_hour == 13:
        print("Добрый день!")
    elif current_hour == 14:
        print("Добрый день!")
    elif current_hour == 15:
        print("Добрый день!")
    elif current_hour == 16:
        print("Добрый день!")
    elif current_hour == 17:
        print("Добрый день!")
    elif current_hour == 18:
        print("Добрый вечер!")
    elif current_hour == 19:
        print("Добрый вечер!")
    elif current_hour == 20:
        print("Добрый вечер!")
    elif current_hour == 21:
        print("Добрый вечер!")
    elif current_hour == 22:
        print("Добрый вечер!")
    else:
        print("Доброй ночи!")

