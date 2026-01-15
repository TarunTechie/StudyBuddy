from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdfData(path):
    loader=PyPDFLoader(path)
    content=loader.load()
    return content
    

def chunking_data(documents):
    splitter=RecursiveCharacterTextSplitter(chunk_size=2000,chunk_overlap=200)
    chunk=splitter.split_documents(documents)
    return chunk
