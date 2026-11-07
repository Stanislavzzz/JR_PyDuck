from my_friends import add_friend as af
from my_friends import remove_friend as rf


friends = ["Боб", "Анна3", "Мэри"]
print(friends)

af.add_f(friends, "Джон")

print(friends)

rf.remove_f(friends, "Боб")

print(friends)