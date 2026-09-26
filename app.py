import json
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger=logging.getLogger(__name__)

def load_documents(path: str) -> list:
    try:
        with open(path, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")

    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON file: {path}")


def validate_document(document: dict) -> bool:
    if not isinstance(document, dict):
        return False

    if (
        "id" in document
        and "title" in document
        and "content" in document
        and isinstance(document["id"], str)
        and isinstance(document["title"], str)
        and isinstance(document["content"], str)
    ):
        return True

    return False


def process_documents(documents: list) -> list:
    processed = []

    for document in documents:

        if not validate_document(document):
           logger.warning("skipping invalid document")
           continue
    
        processed_document = {
            "id": document["id"],
            "title": document["title"],
            "content_length": len(document["content"])
        }

        processed.append(processed_document)

    return processed


def main():
    documents_path=os.getenv("DOCUMENTS_PATH","documents.json")
    documents = load_documents(documents_path)

    valid_documents = [
        document
        for document in documents
        if validate_document(document)
    ]

    processed = process_documents(documents)

    logger.info("Processing completed.")
    print(processed)


if __name__ == "__main__":
    main()