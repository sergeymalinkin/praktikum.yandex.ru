# Замените три точки в условиях правильным логическим оператором and или or
for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")

    if 6 <= current_hour <= 11:
        print('Доброе утро!')
    elif 12 <= current_hour <= 17:
        print('Добрый день!')
    elif 18 <= current_hour <= 22:
        print('Добрый вечер!')
    elif 5 >= current_hour >= 23:
        print('Доброй ночи!')
    else:
        print('Доброй ночи!')

# Научите Анфису правильно называть количество новых сообщений, когда их меньше 100.
# Примените логический оператор or и множественое ветвление с elif, чтобы Анфиса выражалась грамотно.
# К примеру: «У вас 1 новое сообщение», «У вас 35 новых сообщений», «У вас 24 новых сообщения».
# Последнюю цифру удобнее всего получать как остаток при делении на 10.
# В коде этого задания он вычисляется оператором модуло %

# Нужно рассмотреть больше случаев в if-elif-else
for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 11:
        print('У вас ' + str(messages_count) + " новых сообщений")
    elif messages_count == 12:
        print('У вас ' + str(messages_count) + " новых сообщений")
    elif messages_count == 13:
        print('У вас ' + str(messages_count) + " новых сообщений")
    elif messages_count == 14:
        print('У вас ' + str(messages_count) + " новых сообщений")
    elif messages_count == 15:
        print('У вас ' + str(messages_count) + " новых сообщений")
    elif messages_count == 16:
        print('У вас ' + str(messages_count) + " новых сообщений")
    elif messages_count == 17:
        print('У вас ' + str(messages_count) + " новых сообщений")
    elif messages_count == 18:
        print('У вас ' + str(messages_count) + " новых сообщений")
    elif messages_count == 19:
        print('У вас ' + str(messages_count) + " новых сообщений")
    elif remainder == 1:
        print('У вас ' + str(messages_count) + " новое сообщение")
    elif remainder == 0 or remainder >= 5:
        print('У вас ' + str(messages_count) + " новых сообщений")
    else:
        print('У вас ' + str(messages_count) + " новых сообщения")