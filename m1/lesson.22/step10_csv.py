import csv
from pathlib import Path


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "data" / "orders_3.csv"
print(SOURCE)


data = [
    ['order_id', 'client', 'category', 'quantity', 'unit_price', 'status'],
    ['201', 'Анна', 'Книги', '3', '450', 'paid'],
    ['302', 'Борис', 'Канцтовары', '3', '150', 'paid'],
    ['403', 'Олег', 'Книги', '7', '790', 'pending']
]

# data_dict = {
#
# }

with SOURCE.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(
        file,
        delimiter=",",
        fieldnames=data[0]
    )
    writer.writeheader()
    for row in data[1:]:
        my_row = {
            'order_id': row[0],
            'client': row[1],
            'category': row[2],
            'quantity': row[3],
            'unit_price': row[4],
            'status': row[5],
        }
        writer.writerow(my_row)

