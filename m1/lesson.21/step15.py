from pathlib import Path


path_txt = Path("data/javarush.txt")

full = path_txt.resolve()
print(full)

project_path = full.parent.parent
print(project_path)

# # new_path = project_path / "new" / "module" / "python_new.py"
# new_path = project_path / "new/module" / "python_new.py"
#
# print(new_path)


file_path = Path("pyt_file.py")
new_path = project_path / "new/module" / file_path

print(new_path)