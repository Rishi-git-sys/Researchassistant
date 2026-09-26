import logging

from app.validator import validate_document


logger = logging.getLogger(__name__)


def process_documents(documents: list) -> list:
    processed = []

    for document in documents:
        if not validate_document(document):
            logger.warning("Skipping invalid document.")
            continue

        processed_document = {
            "id": document["id"],
            "title": document["title"],
            "content_length": len(document["content"])
        }

        processed.append(processed_document)

    return processed