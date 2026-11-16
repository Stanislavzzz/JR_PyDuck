#
# with open("data/cat.jpg", "rb") as report:
#     content = report.read()
#
#
# print(content)
# print(type(content))



with open("data/cat.jpg", "rb") as report:
    content = report.readlines()


print(content)
print(type(content))