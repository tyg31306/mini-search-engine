from search_engine.persistence import save_index, load_index


def test_save_and_load_index(tmp_path):
    index = {
        "cat": {
            "001": 2,
            "002": 1
        },
        "dog": {
            "001": 1
        }
    }

    index_file = tmp_path / "index.pkl"

    save_index(index, index_file)
    loaded_index = load_index(index_file)

    assert loaded_index == index