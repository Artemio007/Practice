import csv

with open("data/ex.csv", "r") as file:
    reader = csv.reader(file)

    print("Dialect", reader.dialect)


    # построчное считыванрие
    for i in reader:
        print("Line num", reader.line_num)
        print(i)



