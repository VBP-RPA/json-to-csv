import json

from services.csv import *


if __name__ == "__main__":
    with open("input/create.json", "r", encoding="utf-8") as file:
        print(create_csv_template(json.load(file), "output/"))
    with open("input/modify.json", "r", encoding="utf-8") as file:
        print(modify_csv_template(json.load(file), "output/"))
    with open("input/terminate.json", "r", encoding="utf-8") as file:
        print(terminate_csv_template(json.load(file), "output/"))
