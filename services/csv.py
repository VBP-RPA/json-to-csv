from utils.helpers import (
    find_question,
    load_template,
    save_csv,
    success_response,
    error_response,
)

__all__ = ["create_csv_template", "modify_csv_template", "terminate_csv_template"]


def _generate_csv(json_data: dict, output_dir: str, template_path: str) -> str:
    """Generates a CSV file from JSON data and a template.

    Args:
        json_data (dict): Input data.
        output_dir (str): Output directory.
        template_path (str): Template file path.

    Returns:
        str: JSON status string.
    """
    try:
        template_data = load_template(template_path)

        result = f"response_id,,Response ID,{json_data['response_id']}\ndatetime,,Submission Date & Time,{json_data['datetime']}\n\nQuestion,Type"
        for _, section_data in template_data.items():
            result += f"\n,,{section_data['title']}"
            for question in section_data["questions"]:
                id = question["question"]
                label = question["label"]
                answer = find_question(id, json_data)
                result += f'\n"{id}","{answer["type"]}","{label}","{answer["answer"]}"'
            result += "\n"

        output_path = save_csv(
            output_dir, 
            template_path.split("_")[0], 
            json_data.get("response_id", "unknown"),
            result
        )
        return success_response(output_path)

    except Exception as e:
        return error_response(str(e))


def create_csv_template(json_data: dict, output_dir: str) -> str:
    """Generates a CSV file for creating a user.

    Args:
        json_data (dict): Input data.
        output_dir (str): Output directory.

    Returns:
        str: JSON status string.
    """
    return _generate_csv(json_data, output_dir, "create_user.json")


def modify_csv_template(json_data: dict, output_dir: str) -> str:
    """Generates a CSV file for modifying a user.

    Args:
        json_data (dict): Input data.
        output_dir (str): Output directory.

    Returns:
        str: JSON status string.
    """
    return _generate_csv(json_data, output_dir, "modify_user.json")


def terminate_csv_template(json_data: dict, output_dir: str) -> str:
    """Generates a CSV file for terminating a user.

    Args:
        json_data (dict): Input data.
        output_dir (str): Output directory.

    Returns:
        str: JSON status string.
    """
    return _generate_csv(json_data, output_dir, "terminate_user.json")
