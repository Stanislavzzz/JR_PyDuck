from pprint import pprint


report = open("data/javarush.txt", "r", encoding="utf-8")
content = report.readlines()
pprint(content)


report.close()
