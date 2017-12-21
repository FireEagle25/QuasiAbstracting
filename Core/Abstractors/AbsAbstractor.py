import heapq
import sys
from abc import ABCMeta, abstractmethod

from Core.StringSlicing import get_sentences
from Core.WordStorage import WordStorage
from Core.WordsDictionary import WordsDictionary


class AbsAbstractor(metaclass=ABCMeta):

    def __init__(self, text):
        self.sentences = get_sentences(text)
        self.word_storage = WordStorage()
        self.word_storage.push_all_words_from_text(text)
        self.words_dictionary = WordsDictionary("rus_words_db.pickle")

    def truncate(self, prescinde_percent=0.3):

        sentences_count = int((1.0 - prescinde_percent) * len(self.sentences))
        sentences_count = sentences_count if sentences_count > 0 else 1

        weights = self.__get_sentences_weights__()
        print(weights)
        largest_weights = list(set(weights)-set(heapq.nsmallest(sentences_count, weights)))

        self.__print_result_text__(weights, largest_weights)

    def __print_result_text__(self, weights, smallest_weights):
        print("_________________________________________________")
        for index in sorted([weights.index(weight) for weight in smallest_weights]):
            print(self.sentences[index])
        sys.stdout.flush()

    @abstractmethod
    def __get_sentence_weight__(self, sentence):
        pass

    def __get_sentences_weights__(self):
        return [self.__get_sentence_weight__(sentence) for sentence in self.sentences]
