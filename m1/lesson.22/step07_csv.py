import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "data" / "orders.csv"
print(SOURCE)


with SOURCE.open("r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file, delimiter=";")

    for row in reader:
        print(row)