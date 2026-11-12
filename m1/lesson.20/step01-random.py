import random


# print(random.randint(1, 10))
# print(random.random())
# print(random.uniform(1, 10))


# names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names = ("Alice", "Bob", "Charlie", "David", "Eve")
print(random.choice(names))
print(random.choices(names, k=4))
print(random.sample(names, k=3))

# print(random.getrandbits(1))