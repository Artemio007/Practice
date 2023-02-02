import json

data = {
    "fname": "Artem",
    "lname": "Mozalev",
    "age": 24,
    "hobbies": [
        "write",
        "books",
        "sleep"
    ]
}

json_data = json.dumps(data)
print(json_data)


with open("datajson/out.json", "w") as file:

    json.dump(data, file)
    json.