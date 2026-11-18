import pickle


# user_profile = {
#     "username": "John Doe",
#     "level": 7,
#     "items": ["sword", "shield", "potion"]
# }


class User:
    def __init__(self, username, level, items):
        self.username = username
        self.level = level
        self.items = items


user_profile = User("John Doe", 7, ["sword", "shield", "potion"])


with open("data/profile.pickle", "wb") as file:
    pickle.dump(user_profile, file)