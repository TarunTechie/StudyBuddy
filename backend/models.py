from langchain_ollama.chat_models import ChatOllama
from langchain_ollama.embeddings import OllamaEmbeddings

chatModel=ChatOllama(model='llama3.2:latest',
                 top_k=20,
                 temperature=0.7,
                 top_p=0.5)

emdbModel=OllamaEmbeddings(model='embeddinggemma:latest',
                           num_ctx=4096)

