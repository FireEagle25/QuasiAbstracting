import heapq
import math

from Abstractor.StringSlicing import get_words, get_sentences
from Abstractor.WordStorage import WordStorage
from Abstractor.WordsDictionary import WordsDictionary


class Abstractor:

    def __init__(self, text):
        self.sentences = get_sentences(text)
        self.word_storage = WordStorage()
        self.word_storage.add_from_text(text)
        self.words_dictionary = WordsDictionary("rus_words_db.pickle")

    def truncate(self, prescinde_percent=0.3):

        sentences_count = int(prescinde_percent * len(self.sentences))
        sentences_count = sentences_count if sentences_count > 0 else 1

        weights = self.__get_sentences_weights__()
        largest_weights = list(set(weights)-set(heapq.nsmallest(sentences_count, weights)))

        self.__print_result_text__(weights, largest_weights)

    def __print_result_text__(self, weights, smallest_weights):
        print("_________________________________________________")
        for weight in smallest_weights:
            print(self.sentences[weights.index(weight)] + ".")

    def __get_sentence_weight__(self, sentence):
        words = get_words(sentence)
        if len(words) > 0:
            storage = self.word_storage.storage
            return sum([(math.pow(float(self.word_storage.get(word)) / len(storage), 2)) for word in sentence])
        return float('inf')

    def __get_sqr_distance__(self, sentence_x, sentence_y):
        if len(sentence_x) < len(sentence_y):
            sentence_x += [0 for i in range(len(sentence_y) - len(sentence_x))]
        else:
            sentence_y += [0 for i in range(len(sentence_x) - len(sentence_y))]

        return sum(sentence_x - sentence_y) ** 2

    def __get_sentences_weights__(self):
        return [self.__get_sentence_weight__(sentence) for sentence in self.sentences]
