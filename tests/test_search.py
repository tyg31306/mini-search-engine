from search_engine.search import search


def test_single_term_search():
    index = {
        "cat": {
            "001": 2,
            "002": 1
        },
        "dog": {
            "001": 1,
            "002": 2,
            "003": 1
        }
    }

    results = search(index, "cat", 3, 10)

    assert "001" in results
    assert "002" in results
    assert "003" not in results


def test_and_search():
    index = {
        "cat": {
            "001": 2,
            "002": 1
        },
        "dog": {
            "001": 1,
            "002": 2,
            "003": 1
        }
    }

    results = search(index, "cat dog", 3, 10)

    assert "001" in results
    assert "002" in results
    assert "003" not in results


def test_missing_term():
    index = {
        "cat": {
            "001": 2
        }
    }

    results = search(index, "elephant", 1, 10)

    assert results == {}


def test_missing_term_in_multi_word_query():
    index = {
        "cat": {
            "001": 2
        },
        "dog": {
            "001": 1
        }
    }

    results = search(index, "cat elephant", 1, 10)

    assert results == {}


def test_empty_query():
    index = {
        "cat": {
            "001": 2
        }
    }

    results = search(index, "", 1, 10)

    assert results == {}


def test_top_k():
    index = {
        "cat": {
            "001": 5,
            "002": 4,
            "003": 3,
            "004": 2
        }
    }

    results = search(index, "cat", 4, 2)

    assert len(results) == 2


def test_top_k_larger_than_results():
    index = {
        "cat": {
            "001": 5,
            "002": 4
        }
    }

    results = search(index, "cat", 2, 10)

    assert len(results) == 2


def test_results_are_ranked():
    index = {
        "cat": {
            "001": 5,
            "002": 1
        }
    }

    results = search(index, "cat", 2, 10)

    documents = list(results.keys())

    assert documents[0] == "001"