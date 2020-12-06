import re


def between(x, lower, upper):
    return int(x) >= lower and int(x) <= upper

def check_height(x):
    measurement = x[-2:]
    if measurement not in ["cm", "in"]:
        return False
    
    value = x[:-2]
    if measurement == "cm":
        return between(value, 150, 193)
    
    return between(value, 59, 76)

def check_hair_color(x):
    return re.match("^#[0-9a-fA-F]{6}$", x) is not None

checks = {"byr": lambda x: between(x, 1920, 2002),
         "iyr": lambda x: between(x, 2010, 2020),
         "eyr": lambda x: between(x, 2020, 2030),
         "hgt": check_height,
         "hcl": check_hair_color,
         "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
         "pid": lambda x: re.match("^[0-9]{9}$", x) is not None,
         }


def prepare_records(raw_records):
    records = [r.replace("\n", " ") for r in raw_records.split("\n\n")]
    output = []
    for record in records:
        this_cell = {}
        cells = record.split(" ")
        for cell in cells:
            k, v = tuple(cell.split(":"))
            this_cell[k] = v
        output.append(this_cell)

    return output


def quality_checks(records):
    output = []
    for record in records:
        this_record = {"original": record,
                 "is_valid": False,
                 "errors": {}
                 }
        for k, f in checks.items():
            if k not in record:
                this_record['errors'][k] = "missing"
                continue
            this_value = record[k]
            check = f(this_value)
            if not check:
                this_record["errors"][k] = f"Failed check: {this_value}"
        
        if this_record["errors"] == {}:
            this_record["is_valid"] = True
        
        output.append(this_record)
    return output



inputs = open("inputs/04.txt", "r").read()
records = prepare_records(inputs)
q = quality_checks(records)
output = {"pass": 0, "fail": 0}
for record in q:
    if record["is_valid"] == True:
        output["pass"] += 1
    else:
        output["fail"] += 1

import pandas as pd
pd.DataFrame([r["original"] for r in q if r["is_valid"]]).to_excel("output.xlsx")
print(q)
