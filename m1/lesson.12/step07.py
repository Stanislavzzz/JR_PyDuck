def greet_name(name='User', age=0):
    print('Как тебя зовут?')
    result = age + 10
    print(f'Пока, {name}, {result} лет')


greet_name(name='Bob', age=22)
print()
greet_name(age=27, name='Anna')
print()
greet_name(age=19)
print()
greet_name(name='Mary')
print()
greet_name()




