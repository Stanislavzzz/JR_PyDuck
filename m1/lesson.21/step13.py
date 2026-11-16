from pathlib import Path


# path_txt = Path("data/javarush.txt")
path_txt = Path("data")


# for i in path_txt.iterdir():
#     print(i)

# for i in path_txt.glob("*.txt"):
#     print(i)

for i in path_txt.rglob("*.txt"):
    print(i)

