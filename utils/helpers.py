import os
import json


def find_question(question_id: str, json_data: dict) -> dict:
    """Finds a question by ID.

    Args:
        question_id (str): Question ID.
        json_data (dict): Input data.

    Returns:
        dict: Answer dictionary, empty if not found.
    """
    for answer in json_data["answers"]:
        if answer["question"] == question_id:
            return answer
    return {"question": question_id, "answer": "", "type": ""}


def load_template(template_path: str) -> dict:
    """Loads a JSON template.

    Args:
        template_path (str): Template file path.

    Returns:
        dict: Template data.
    """
    with open(os.path.join("templates", template_path), "r", encoding="utf-8") as file:
        return json.load(file)


def success_response(data: str) -> str:
    """Creates a success JSON response.

    Args:
        data (str): Response data.

    Returns:
        str: JSON string.
    """
    return json.dumps({"status": "SUCCESS", "status_code": 200, "data": data})


def error_response(error: str) -> str:
    """Creates an error JSON response.

    Args:
        error (str): Error message.

    Returns:
        str: JSON string.
    """
    return json.dumps({"status": "ERROR", "status_code": 400, "error": error})


def save_csv(output_dir: str, file_prefix: str, response_id: str, content: str) -> str:
    """Saves CSV content to file.

    Args:
        output_dir (str): Output directory.
        file_prefix (str): File prefix.
        response_id (str): Response ID.
        content (str): CSV content.

    Returns:
        str: File path.
    """
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{file_prefix}_{response_id}.csv"
    output_path = os.path.join(output_dir, filename)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

    return output_path
