import os
from app.loader import load_documents
from app.processor import process_documents
import logging

def main():
    logger=logging.basicConfig(level=logging.INFO, format ='%(asctime)s -%(levelname)s - %(message)s')
    logger=logging.getLogger(__name__)

    documents_path=os.getenv("DOCUMENTS_PATH","documents.json")
    documents=load_documents(documents_path)

    processed=process_documents(documents)

    logger.info("Processing completed.")
    print(processed)



if __name__=="__main__":
    main()


