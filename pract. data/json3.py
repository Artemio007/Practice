import json
import datetime


data = {
    "fname": "Artem",
    "lname": "Mozalev",
    "birthday": datetime.date(1986, 9, 29),
    "hired_add": datetime.datetime(2006, 9, 29, 12, 30, 5),
    "hobbies": [
        "write",
        "books",
        "sleep",
        "guitar"
    ]
}

#
# json_data = json.dump(data)

class DateFormatEncoder(json.JSONEncoder):

    def to_default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                "value": obj.strftime("%d/%m/%y %H:%M:%S"),
                "datetime": True
            }
        elif isinstance(obj, datetime.date):
            return {
                "value": obj.strftime("%d/%m/%y"),
                "date": True
            }

        return json.JSONEncoder.default(self, obj)


json_data = json.dumps(data, cls=DateFormatEncoder, indent=4, default=str)
print(json_data)
