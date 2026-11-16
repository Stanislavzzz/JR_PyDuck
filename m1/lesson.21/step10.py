# report = open("data/javarush.txt", "r", encoding="utf-8")
# content = report.read()
# report.close()
#
# print(content)
# print(type(content))


with open("data/javarush.txt", "r", encoding="utf-8") as report:
    content = report.read()


print(content)
print(type(content))