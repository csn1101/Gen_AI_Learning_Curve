from langchain.document_loaders.pdf import PyPDFDirectoryLoader
def load_documents(data_path):
    document_loader = PyPDFDirectoryLoader(data_path)
    return document_loader.load()