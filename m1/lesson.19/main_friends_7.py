import my_friends.add_friend
import my_friends.remove_friend


friends = ["Боб", "Анна", "Мэри"]
print(friends)

my_friends.add_friend.add_f(friends, "Джон")

print(friends)

my_friends.remove_friend.remove_f(friends, "Боб")

print(friends)