import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "data" / "orders_2.csv"
print(SOURCE)


data = [
    ['order_id', 'client', 'category', 'quantity', 'unit_price', 'status'],
    ['101', 'Анна', 'Книги', '2', '450', 'paid'],
    ['102', 'Борис', 'Канцтовары', '3', '150', 'paid'],
    ['103', 'Олег', 'Книги', '1', '790', 'pending']
]


with SOURCE.open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerows(data)