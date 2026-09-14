from search_engine.tokenizer import tokenize


def test_basic_tokenization():
    result = tokenize("Hello hello world")
    assert result == {"hello": 2, "world": 1}


def test_punctuation_removal():
    result = tokenize("Hello, world! How are you?")
    assert result == {"hello": 1, "world": 1, "how": 1, "you": 1}


def test_stop_words_removed():
    result = tokenize("the cat is on the mat")
    assert result == {"cat": 1, "mat": 1}


def test_repeated_words():
    result = tokenize("cat cat cat dog dog")
    assert result == {"cat": 3, "dog": 2}


def test_empty_text():
    result = tokenize("")
    assert result == {}
