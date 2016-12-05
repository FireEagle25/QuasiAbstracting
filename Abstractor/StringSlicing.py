import re


def get_words(text):
    words = [word for word in re.split('n|\s|\)|\(|,|\.|-', text) if len(word) > 0]
    return words


def get_sentences(text):
    sentences = [sentence for sentence in re.split('\n|\.', text) if len(sentence) > 0]
    return sentences