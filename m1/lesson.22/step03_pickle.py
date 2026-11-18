import pickle


user_profile = {
    "username": "John Doe",
    "level": 7,
    "items": ["sword", "shield", "potion"]
}


# class User:
#     def __init__(self, username, level, items):
#         self.username = username
#         self.level = level
#         self.items = items
#
#
# user_profile = User("John Doe", 7, ["sword", "shield", "potion"])


byte_data = pickle.dumps(user_profile)
print(f"Сериализовали {byte_data}")
print(type(byte_data))


restored_profile = pickle.loads(byte_data)
print(f"Десериализовали {restored_profile}")
print(type(restored_profile))

