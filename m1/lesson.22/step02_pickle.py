import pickle
from step01_pickle import User


with open("data/profile.pickle", "rb") as file:
    load_data = pickle.load(file)


print(load_data)
print(load_data.username)
print(load_data.level)