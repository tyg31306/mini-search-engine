import re

STOP_WORDS = {
    "a", "an", "the",
    "and", "or", "but",
    "is", "are", "was", "were",
    "in", "on", "at", "to",
    "of", "for", "with",
    "this", "that", "these", "those"
}

def clean(text):
    return re.sub(r'[^\w\s]', '', text)

def tokenize(text):
    words = clean(text).lower().split()
    words = [word for word in words if word not in STOP_WORDS]
    occurrences = {}
    for word in words:
        if word not in occurrences:
            occurrences[word] = 1
        else:
            occurrences[word] += 1
    return occurrences

