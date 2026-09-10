from pathlib import Path
from index import build_index
from search import search
from snippets import get_snippet
DOCUMENT_DIR = Path("../data/documents")
num_documents = 10000
index = build_index(DOCUMENT_DIR, num_documents)
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

