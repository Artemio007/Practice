import csv


class DialectCustom(csv.Dialect):
    quoting = csv.QUOTE_ALL
    delimiter = "|"
    lineterminator = "\n"
    quotechar = "*"


csv.register_dialect("testdialect", dialect=DialectCustom)


with open("data/output1.csv", "w") as file:
    writer = csv.writer(file, dialect=DialectCustom)
    writer.writerow([1, 2, 3, 4])
    writer.writerow([1, 2, 3, 4])
    writer.writerow([1, 2, 3, 4])
    writer.writerow([1, 2, 3, 4])