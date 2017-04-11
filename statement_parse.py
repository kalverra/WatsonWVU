import json
import csv

csv_writer = csv.writer(open("statements.csv", "w"))
statements = json.load(open("statements.json", "r"))

csv_writer.writerow(["Statement", "Ruling", "Economics (T/F)"])

for statement in statements:
    about_economy = "F"
    for subject in statement["subject"]:
        if subject["subject_slug"] == "economy":
            about_economy = "T"
    csv_writer.writerow([
       "\""+ statement["ruling_headline"].encode("ascii", "ignore")+"\"",
        statement["ruling"]["ruling"].encode("ascii", "ignore"),
        about_economy
    ])
