from pathlib import Path
from index import build_index
from search import search
DOCUMENT_DIR = Path("../data/documents")

index = build_index(DOCUMENT_DIR, 100)
while True:
    query = input("> ")
    results = search(index, query)
    print(results)


