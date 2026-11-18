import yaml


report = {
    'shop': {
        'name': 'JavaRush1',
        'address': 'Moscow1',
        'category': ['Книги', 'Курсы'],
        'menu': None
    }
}

with open('data/report.yaml', 'w', encoding='utf-8') as file:
    yaml.safe_dump(
        report,
        file,
        default_flow_style=False,
        allow_unicode=True
    )


with open('data/test.yaml', 'r', encoding='utf-8') as file:
    data_dict = yaml.safe_load(file)
    print(data_dict)
    print(type(data_dict))
