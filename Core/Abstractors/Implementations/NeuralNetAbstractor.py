import sys

from Core.Abstractors.Abstractor import Abstractor
from Core.StringSlicing import get_words
from NeuralNet.NeuralNet import Net


class NeuralNetAbstractor(Abstractor):

    def __init__(self, text, neural_net_file):
        super().__init__(text)
        self.net = Net.create_from_file(neural_net_file)

    def __get_sentence_weight__(self, sentence):
        weight = self.net.net.activate(self.convert_sentence_to_neural_net_params(sentence))[0]
        print(self.convert_sentence_to_neural_net_params(sentence), weight)
        return weight

    def convert_sentence_to_neural_net_params(self, sentence):
        words = get_words(sentence)
        return [len(sentence),
               len(words),
               min([len(word) for word in words]),
               max([len(word) for word in words]),
               sum([self.words_dictionary.get_freq(word) for word in words])]

    def __print_result_text__(self, weights, largest_weights):
        print("_________________________________________________")
        weight_usages = {}
        for index in sorted([weights.index(weight) for weight in largest_weights]):

            if index not in weight_usages.keys():
                weight_usages[index] = 0
            weight_usages[index] += 1

            print(self.sentences[index + weight_usages[index]])
        sys.stdout.flush()
