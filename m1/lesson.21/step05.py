report = open("data/javarush.txt", "r", encoding="utf-8")
content = report.readline()
print(content)
print("*" * 50)

content = report.readline()
print(content)

report.close()
