# encoding: utf-8
#!/usr/bin/env python3
import csv
import json
from time import gmtime, strftime


def csv_json(csv_file, json_file):
    json_array = []

    with open(csv_file, encoding="utf-8") as csv_f:
        csv_reader = csv.DictReader(csv_f)
        for row in csv_reader:
            json_array.append(row)

    with open(json_file, "w", encoding="utf-8") as json_f:
        json_str = json.dumps(json_array)
        json_f.write(json_str)


csv_file_path = "titanic.csv"
json_file_path = "passengers/fixtures/titanic.json"

if __name__ == "__main__":
    csv_json(csv_file_path, json_file_path)

print("CSV converted to JSON")
print("Logged:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
