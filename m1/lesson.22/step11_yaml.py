import yaml


yaml_text = """shop:
  name: JavaRush
  address: Moscow
  category:
    - Книги
    - Курсы
  menu: null
"""

data_dict = yaml.safe_load(yaml_text)
print(data_dict)
print(type(data_dict))


