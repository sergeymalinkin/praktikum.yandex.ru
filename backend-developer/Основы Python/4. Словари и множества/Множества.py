# Сделайте из списка cities сет unique_cities, где записаны по разу названия городов,
# в которых живут ваши друзья. После этого напечатайте строку из элементов
# unique_cities на экран через запятую — да, join() работает и для множеств тоже!

cities = ['Вологда', 'Чебоксары', 'Тольятти', 'Вологда']

unique_cities = set(cities)
print(", " .join(set(cities)))

# Для каждого уникального города в списке cities напечатайте на экран сообщение Один мой друг живёт в городе <название города>.
cities = ['Санкт-Петербург', 'Хабаровск', 'Казань', 'Санкт-Петербург', 'Казань']

# напишите ваш код здесь
unique_cities = set(cities)
for city in unique_cities:
    print("Один мой друг живет в городе " + city)