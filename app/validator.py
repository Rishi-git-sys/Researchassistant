from app.types import Document

def validate_document(document: Document) -> bool:
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