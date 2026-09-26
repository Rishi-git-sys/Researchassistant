import pytest
from app import validate_document,load_documents,process_documents


def test_valid_document():
    document = {
        "id": "doc-001",
        "title": "Introduction to AI Agents",
        "content": "AI agents can use tools."
    }

    assert validate_document(document) is True


def test_missing_content():
    document = {
        "id": "doc-002",
        "title": "RAG Fundamentals"
    }

    assert validate_document(document) is False

def test_empty_document():
    document = {}

    assert validate_document(document) is False

def test_load_documents():
    documents=load_documents("documents.json")

    assert len(documents) == 2

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_documents("does_not_exist.json")   

def test_invalid_json():
    with pytest.raises(ValueError):
        load_documents("bad.json") 

def test_invalid_content_type():
    document={
        "id": "doc-001",
        "title": "Test",
        "content": 12345
    }
    assert validate_document(document) is False

def test_invalid_document_type():
    assert validate_document("hello") is False    

def test_process_documents():
    documents = [
        {
            "id": "doc-001",
            "title": "AI Agents",
            "content": "AI agents can use tools."
        }
    ]

    result = process_documents(documents)

    assert len(result) == 1
    assert result[0]["id"] == "doc-001"
    assert result[0]["title"] == "AI Agents"
    assert result[0]["content_length"] == 24    