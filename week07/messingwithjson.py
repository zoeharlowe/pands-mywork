# messingwithjson.py
# Writing a dict to a json file
# Author: Zoe McNamara Harlowe

import json

FILENAME = "student_data.json"

def write_dict(obj):
    with open (FILENAME, "wt") as f:
        json.dump(obj, f)

FILENAME2 = "test.json"

def read_dict():
    with open(FILENAME2) as f:
        return json.load(f)

mydict = read_dict()
print(mydict)