import json


def load_documents(path: str) -> list:
    try:
        with open(path, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")

    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON file: {path}")