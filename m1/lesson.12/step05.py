def greet_name(name, age=0):
    print('Как тебя зовут?')
    result = age + 10
    print(f'Пока, {name}, {result} лет')




greet_name('Bob')
print()
greet_name(input("Введите имя: "), int(input("Введите возраст: ")))
print()
print()
my_name = 'Mary'
my_age = 19

greet_name(my_name)



