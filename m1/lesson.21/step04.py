report = open("data/javarush.txt", "r", encoding="utf-8")

for line in report:
    print(line)


report.close()