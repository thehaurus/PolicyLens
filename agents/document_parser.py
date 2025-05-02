import tempfile
from langchain.document_loaders import PyPDFLoader

def run(state):
    uploaded_file = state["pdf"]

    # Write uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    loader = PyPDFLoader(tmp_path)
    pages = loader.load()
    full_text = "\n".join([page.page_content for page in pages])
    return {**state, "raw_text": full_text}


# from langchain.document_loaders import PyPDFLoader

# def run(state):
#     pdf = state["pdf"]
#     loader = PyPDFLoader(pdf)
#     pages = loader.load()
#     full_text = "\n".join([page.page_content for page in pages])
#     return {**state, "raw_text": full_text}
