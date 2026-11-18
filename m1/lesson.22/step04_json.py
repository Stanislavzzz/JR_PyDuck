# {
#     "country": "USA",
#     "username": "John Doe",
#     "level": 7,
#     "isEurop": false,
#     "items": ["sword", "shield", "potion"],
#     "subjects": {
#         "user": "Bob",
#         "age": 25,
#     },
# }

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


json_string = json.dumps(employees, indent=4)

print(json_string)
print(type(json_string))


data = json.loads(json_string)
print(data)
print(type(data))