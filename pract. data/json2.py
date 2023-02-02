import json

data = '{"fname": "Artemm","lname": "Mozzalev", "age": 23, "hobbies": ["write","books","sleep"]}'

data_ = json.loads(data)
print(type(data_))
print(type(data))


with open("datajson/out1.json", "r") as file:
    j_d = json.load(file)
    print(j_d)
