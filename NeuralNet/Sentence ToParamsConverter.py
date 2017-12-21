from Core.StringSlicing import get_words


def convert_sentence_to__neural_net_params(sentence, abstractor):
    words = get_words(sentence)
    return len(sentence), \
           len(words), \
           min([len(word) for word in words]), \
           max([len(word) for word in words]), \
           sum([abstractor.words_dictionary.get_freq(word) for word in words]),
