from pymystem3 import Mystem
from Abstractor.StringSlicing import get_words


class WordStorage:
    def __init__(self):
        self.storage = {}
        self.m = Mystem()

    def add_from_text(self, text):
        for word in get_words(text):
            self.add(word)

    def add(self, word):
        normalized_word = self.m.lemmatize(word)[0]

        if normalized_word in self.storage.keys():
            self.storage[normalized_word] += 1
        else:
            self.storage[normalized_word] = 1

    def get(self, word):
        normalized_word = self.m.lemmatize(word)[0]

        if normalized_word in self.storage.keys():
            return self.storage[normalized_word]

        return 0

    def __str__(self):

        all_words = ""

        for word in self.storage:
            all_words += word + " " + str(self.storage[word]) + "\n"

        return all_words