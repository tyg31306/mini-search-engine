from tokenizer import tokenize

def search(index, query):
    query = query.lower().strip()

    document_sets = []
    terms = tokenize(query)
    relevance_scores = dict()

    if len(terms) == 0:
        return set()
    for term in terms:
        if term not in index:
            return set()
        else:
            document_sets.append(set(index[term]))
    matching_docs = set.intersection(*document_sets)
    for doc in matching_docs:
        relevance_scores[doc] = 0
        for term in terms:
            relevance_scores[doc] += index[term][doc]
    return dict(sorted(relevance_scores.items(), key=lambda item: item[1], reverse=True))
