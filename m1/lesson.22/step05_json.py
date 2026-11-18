import json


employees = {
    "country": "USA",
    "username": "John Doe",
    "level": 7,
    "isEurop": False,
    "items": ["sword", "shield", "potion"],
    "subjects": {
        "user": "Bob",
        "age": 25,
    },
}


print(employees)
print(type(employees))


with open("data/employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)




