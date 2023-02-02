import csv

with open("data/ex.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # print(row)
        print(row.get("name"))