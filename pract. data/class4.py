import csv


quoting = csv.QUOTE_ALL

with open("data/output.csv", "w") as file:
    writer = csv.DictWriter(file,
                            fieldnames=["fname", "lname", "age"],
                            quoting=quoting
                            )
    writer.writeheader()
    writer.writerow(
        {
            "fname": "Artem",
            "lname": "Mozalev",
            "age": 24
        }
    )
    writer.writerow(
        {
            "fname": "Aliaksandr",
            "lname": "Holybey",
            "age": 29
        }
    )
    writer.writerow(
        {
            "fname": "Sasha",
            "lname": "Gray",
            "age": 26
        }
    )