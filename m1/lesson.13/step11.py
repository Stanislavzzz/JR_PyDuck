friends = [
    {"name": "John", "age": 25},
    {"name": "Ivan", "age": 30},
    {"name": "Anna", "age": 43},
    {"name": "Bob", "age": 17},
]

# sorted_friends = sorted(friends)
# print(sorted_friends)


sorted_friends = sorted(friends, key=lambda friend: friend["age"])
print(sorted_friends)

