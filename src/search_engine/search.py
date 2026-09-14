from search_engine.tokenizer import tokenize
import math

def search(index, query, num_docs, k=10):
    query = query.lower().strip()

    document_sets = []
    terms = tokenize(query)
    relevance_scores = dict()

    if len(terms) == 0:
        return {}

    for term in terms:
        if term not in index:
            return {}
        else:
            document_sets.append(set(index[term]))

    matching_docs = set.intersection(*document_sets)

    for doc in matching_docs:
        relevance_scores[doc] = 0
        for term in terms:
            idf = math.log(num_docs / len(index[term]))
            tf = index[term][doc]
            relevance_scores[doc] += tf * idf

    sorted_results = sorted(
        relevance_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return dict(sorted_results[:k])
