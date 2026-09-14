from search_engine import snippets


def test_snippet_contains_query(tmp_path):
    document = tmp_path / "001.txt"
    document.write_text(
        "The patient was feeling sick after the procedure.",
        encoding="utf-8"
    )

    snippets.DOCUMENT_DIR = tmp_path

    result = snippets.get_snippet("001", "sick")

    assert "sick" in result


def test_snippet_removes_newlines(tmp_path):
    document = tmp_path / "001.txt"
    document.write_text(
        "The patient was\nfeeling sick\nafter the procedure.",
        encoding="utf-8"
    )

    snippets.DOCUMENT_DIR = tmp_path

    result = snippets.get_snippet("001", "sick")

    assert "\n" not in result


def test_snippet_is_shorter_than_document(tmp_path):
    document = tmp_path / "001.txt"
    document.write_text(
        "This is a very long document containing a sick person "
        "who needed medical attention.",
        encoding="utf-8"
    )

    snippets.DOCUMENT_DIR = tmp_path

    result = snippets.get_snippet("001", "sick")

    assert len(result) < len(document.read_text(encoding="utf-8"))
