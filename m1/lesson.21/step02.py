# report = open("data/javarush.txt", "r", encoding="utf-8")
# content = report.read(50)
# print(content)
#
# print("*" * 50)
#
# content = report.read(50)
# print(content)
#
# report.close()\


report = open("data/javarush.txt", "r", encoding="utf-8")

chunk_size = 50
content = report.read(chunk_size)

while content:
    print(content)
    content = report.read(chunk_size)
    print("*" * 50)




report.close()