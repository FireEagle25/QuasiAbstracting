import heapq

from Abstractor.StringSlicing import get_words, get_sentences
from Abstractor.WordStorage import WordStorage


class Abstractor:

    def __init__(self, text):
        self.sentences = get_sentences(text)
        self.world_storage = WordStorage()
        self.world_storage.add_from_text(text)

    def truncate(self, prescinde_percent=0.3):

        sentences_count = int(prescinde_percent * len(self.sentences))
        sentences_count = sentences_count if sentences_count > 0 else 1

        weights = self.__get_sentences_weights__()
        smallest_weights = heapq.nsmallest(sentences_count, weights)
        self.__print_result_text__(weights, smallest_weights)

    def __print_result_text__(self, weights, smallest_weights):
        print("_________________________________________________")
        for weight in smallest_weights:
            print(self.sentences[weights.index(weight)] + ".")

    def __get_sentence_weight__(self, sentence):
        words = get_words(sentence)
        return sum([self.world_storage.get(word) for word in words]) / len(words)

    def __get_sentences_weights__(self):
        return [self.__get_sentence_weight__(sentence) for sentence in self.sentences]
