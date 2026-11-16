name_list = ["Anna\n", "Mike\n", "Bob\n", "Mila\n", "Igor\n"]


report = open("data/names.txt", "w", encoding="utf-8")

report.writelines(name_list)

report.close()
