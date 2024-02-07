from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
import re

# load the directory
def context(option): 
    print("inside ingest.py", option)
    if option == 'Calculus 1':
        pdf_file_path = 'app/Knowledge Base/Calculus'
    elif option == 'Physics':
        pdf_file_path = 'app/Knowledge Base/Physics'
    elif option == 'Computer Science':
        pdf_file_path = 'app/Knowledge Base/Computer Science'
    elif option == 'Finance':
        pdf_file_path = 'app/Knowledge Base/Finance'
      
    loader = PyPDFDirectoryLoader(pdf_file_path)
    data = loader.load()

    print(len(data))
    # chunk the data
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=0.25)
    data = text_splitter.split_documents(data)

    for document in data:
        document.page_content = preprocess(document.page_content)

    return data

def preprocess(text):
    # Remove '\xa0' (non-breaking space)
    text = re.sub(r'\xa0', ' ', text)

    # Remove '\n' (newlines)
    text = re.sub(r'\n', ' ', text)

    # Remove consecutive dots ('.....') with just one dot
    text = re.sub(r'\.{2,}', '', text)

    # Remove '\uf0b7'
    text = re.sub(r'\uf0b7', ' ', text)

    # Remove consecutive spaces
    text = re.sub(r' +', ' ', text)

    return text

