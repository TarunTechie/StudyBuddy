from langchain_chroma import Chroma
from models import emdbModel


def addData(document,id,collectionName):
    print(f"Adding data to {collectionName}")
    vectorDb=Chroma(
        embedding_function=emdbModel,
        persist_directory='./testing/chroma_db',
        collection_name=collectionName
    )
    vectorDb.add_documents(documents=document,ids=id)
    

def getData(query,collectionName):
    print(f"Getting data from {collectionName}")
    vectorDb=Chroma(embedding_function=emdbModel,
                    persist_directory='./testing/chroma_db',
                    collection_name=collectionName)
    results=vectorDb.similarity_search(query,k=1)
    return results