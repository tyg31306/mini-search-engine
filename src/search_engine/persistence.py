import pickle
from pathlib import Path


def save_index(index, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(index, file)


def load_index(file_path):
    with open(file_path, "rb") as file:
        return pickle.load(file)