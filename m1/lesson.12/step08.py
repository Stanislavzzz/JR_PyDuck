def greet_name(name='User', age=0, city='Moscow', language='English'):
    print('Как тебя зовут?')
    result = age + 10
    print(f'Пока, {name}, {result} лет, город - {city}, язык - {language}')


# greet_name('Bob', 22, "Sochi", "Russian")
# greet_name(name='Bob', 22, "Sochi", "Russian") # ошибка
greet_name('Bob', 22, language="Russian", city="Sochi")




