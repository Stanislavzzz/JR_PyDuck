name_list = ["Anna\n", "Mike\n", "Bob\n", "Mila\n", "Igor\n"]


report = open("data/names2.txt", "a", encoding="utf-8")

report.writelines(name_list)

report.close()
