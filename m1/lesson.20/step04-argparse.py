import argparse


parser = argparse.ArgumentParser()
parser.add_argument("name", help="Имя пользователя")
parser.add_argument("age", help="Возраст пользователя")
parser.add_argument("--lang", default="ru", help="Язык приветствия")
args = parser.parse_args()
print(args)

if args.lang == "ru":
    print(f'Привет, {args.name}, тебе {args.age} лет')
elif args.lang == "en":
    print(f'Hello, {args.name}, you are {args.age} years old')
else:
    print(f'Неизвестный язык -  {args.name} - {args.age}')