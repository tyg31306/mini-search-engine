from tokenizer import tokenize

def search(index, query):
    query = query.lower().strip()

    setlist = list()
    terms = tokenize(query)

    if len(terms) == 0:
        return set()
    for term in terms:
        if term not in index:
            return set()
        else:
            setlist.append(index[term].keys())
    return set.intersection(*setlist)
