from itertools import islice
from search_engine.tokenizer import tokenize

def build_index(document_dir, num_documents=None):
    index = {}
    files = sorted(document_dir.glob("*.txt"))
    if num_documents is not None:
        files = islice(files, num_documents)

    for file_path in files:
        doc_id = file_path.stem
        raw = file_path.read_text(encoding="utf-8")
        occurrence = tokenize(raw)
        for word, count in occurrence.items():
            if word not in index:
                index[word] = {}
            index[word][doc_id] = count
    return index