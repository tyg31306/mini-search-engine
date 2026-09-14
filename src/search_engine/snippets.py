from pathlib import Path
from search_engine.tokenizer import tokenize

DOCUMENT_DIR = Path("../../data/documents")
def get_snippet(doc_path, query):
    file_path = DOCUMENT_DIR / f"{doc_path}.txt"
    text = file_path.read_text(encoding="utf-8")

    terms  = tokenize(query)
    term = next(iter(terms))
    q_index = text.lower().find(term)

    start = q_index - 20
    end = q_index + 20

    while start > 0 and not text[start].isspace():
        start -= 1
    while end < len(text) and not text[end].isspace():
        end += 1

    snippet = text[start:end]
    snippet = " ".join(snippet.split())
    return "..." + snippet + "..."
