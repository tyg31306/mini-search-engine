from search_engine.index import build_index


def test_build_index(tmp_path):
    document_1 = tmp_path / "001.txt"
    document_2 = tmp_path / "002.txt"

    document_1.write_text("cat cat dog", encoding="utf-8")
    document_2.write_text("cat dog dog", encoding="utf-8")

    index = build_index(tmp_path)

    assert index["cat"]["001"] == 2
    assert index["cat"]["002"] == 1
    assert index["dog"]["001"] == 1
    assert index["dog"]["002"] == 2


def test_term_in_correct_documents(tmp_path):
    document_1 = tmp_path / "001.txt"
    document_2 = tmp_path / "002.txt"

    document_1.write_text("cat dog", encoding="utf-8")
    document_2.write_text("bird dog", encoding="utf-8")

    index = build_index(tmp_path)

    assert "001" in index["cat"]
    assert "002" not in index["cat"]


def test_missing_term(tmp_path):
    document = tmp_path / "001.txt"
    document.write_text("cat dog", encoding="utf-8")

    index = build_index(tmp_path)

    assert "elephant" not in index
