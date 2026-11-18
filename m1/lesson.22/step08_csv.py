import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "data" / "orders.csv"
print(SOURCE)


with SOURCE.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")
    print(reader.fieldnames)

    for row in reader:
        print(row.get("order_id"), row.get("client"), row.get("category"), row.get("quantity"))