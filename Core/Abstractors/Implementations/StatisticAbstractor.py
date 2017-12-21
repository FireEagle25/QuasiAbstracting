from Core.Abstractors.AbsAbstractor import AbsAbstractor
from Core.StringSlicing import get_words


class StatisticAbstractor(AbsAbstractor):

    def __get_sentence_weight__(self, sentence):
        words = get_words(sentence)
        if len(words) > 0:
            return sum([(float(self.word_storage.get_frequency(word)) * (
                    1.0 / self.words_dictionary.get_freq(self.word_storage.get_stemmed(word))) / len(
                self.word_storage.storage)) ** 2 for word in sentence])
        return float('inf')

    @staticmethod
    def __get_sqr_distance__(sentence_x, sentence_y):
        if len(sentence_x) < len(sentence_y):
            sentence_x += [0 for _ in range(len(sentence_y) - len(sentence_x))]
        else:
            sentence_y += [0 for _ in range(len(sentence_x) - len(sentence_y))]

        return sum(sentence_x - sentence_y) ** 2