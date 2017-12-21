from pymystem3 import Mystem
from Core.StringSlicing import get_words
from Core.WordsDictionary import WordsDictionary


class WordStorage:
    def __init__(self):
        self.storage = {}
        self.m = Mystem()
        self.words_dictionary = WordsDictionary("rus_words_db.pickle")

    def push_all_words_from_text(self, text):
        for word in get_words(text):
            self.push(word)

    def push(self, word):

        normalized_word = self.m.lemmatize(word)[0]

        words = [normalized_word] + self.words_dictionary.get_synonyms(normalized_word)

        for word in words:
            if word in self.storage.keys():
                self.storage[word] += 1
            else:
                self.storage[word] = 1

    def get_frequency(self, word):
        normalized_word = self.m.lemmatize(word)[0]

        if normalized_word in self.storage.keys():
            return self.storage[normalized_word]

        return 0

    def get_stemmed(self, word):
        return self.m.lemmatize(word)[0]

    def __str__(self):

        all_words = ""

        for word in self.storage:
            all_words += word + " " + str(self.storage[word]) + "\n"

        return all_words