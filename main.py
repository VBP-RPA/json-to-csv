import json
import os
from dotenv import load_dotenv
from services.csv import *

load_dotenv()


def main():
    create_path = os.getenv("JSON_CREATE_DIR", "")
    modify_path = os.getenv("JSON_MODIFY_DIR", "")
    terminate_path = os.getenv("JSON_TERMINATE_DIR", "")
    output_path = os.getenv("CSV_OUTPUT_DIR", "")

    process_path(create_path, output_path, create_csv_template)
    process_path(modify_path, output_path, modify_csv_template)
    process_path(terminate_path, output_path, terminate_csv_template)


def process_path(input_path: str, output_path: str, processor):
    if os.path.isfile(input_path):
        files = [input_path]
    elif os.path.isdir(input_path):
        files = sorted(
            os.path.join(input_path, file_name)
            for file_name in os.listdir(input_path)
            if file_name.lower().endswith(".json")
        )
    else:
        return

    if not files:
        return

    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as file:
            print(processor(json.load(file), output_path))


if __name__ == "__main__":
    main()
