from pathlib import Path

from search_engine.index import build_index
from search_engine.search import search
from search_engine.snippets import get_snippet
from search_engine.persistence import save_index, load_index
INDEX_FILE = Path("data/index.pkl")
DOCUMENT_DIR = Path("../../data/documents")
num_documents = 10000
if INDEX_FILE.exists():
    print("Existing index loaded.")
    index = load_index(INDEX_FILE)
else:
    print("Building index...")
    index = build_index(DOCUMENT_DIR, num_documents)

    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    save_index(index, INDEX_FILE)

    print("Index saved.")

while True:
    user_input = input("> ")
    k = 10
    if "--top" in user_input:
        parts = user_input.split()
        top_index = parts.index("--top")

        query = " ".join(parts[:top_index])

        try:
            k = int(parts[top_index + 1])
        except (ValueError, IndexError):
            print("Error: --top requires a positive integer")
            continue
        if k <= 0:
            print("Error: --top requires a positive integer")
            continue
    else:
        query = user_input
    results = search(index, query, num_documents, k)
    print(f"Document       Score\n--------------------")
    for doc, score in results.items():
        print(f"{doc}    {score:>10.4f}")
        print(get_snippet(doc, query))
        print("\n")

