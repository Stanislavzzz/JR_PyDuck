import my_friends.add_friend as a_f
import my_friends.remove_friend as r_f


friends = ["Боб", "Анна", "Мэри"]
print(friends)

a_f.add_f(friends, "Джон")

print(friends)

r_f.remove_f(friends, "Боб")

print(friends)