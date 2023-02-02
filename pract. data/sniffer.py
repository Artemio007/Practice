import csv


sniffer = csv.Sniffer()
dialect = None

# with open("data/ex.csv", "r") as file:
#     reader = csv.reader(file)
#
#     for i in reader:
#         print(i)


with open("data/ex.csv", "r") as file:
    context = file.read()
    dialect = sniffer.sniff(context)
    print(dialect.delimiter, dialect.quotechar, dialect.quoting)

