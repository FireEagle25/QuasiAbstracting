import pickle


class WordsDictionary:

    def __init__(self, dictionary_file):
        with open(dictionary_file, 'rb') as handle:
            self.dict = pickle.load(handle)

    def get_synonyms(self, word):
        try:
            row = self.dict[word]
            if len(row) >= 2:
                return row[1]
        except KeyError:
            pass
        return []

    def get_freq(self, word):
        try:
            return self.dict[word][0]
        except KeyError:
            return 0.1

    def get_full_info(self, word):
        try:
            return self.dict[word]
        except KeyError:
            return []