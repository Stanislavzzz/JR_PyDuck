import json



with open("data/employees.json", "r", encoding="utf-8") as file:
    employees = json.load(file)


print(employees)
print(type(employees))




