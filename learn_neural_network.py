from NeuralNet.NeuralNet import Net


def main():
    net = Net()
    net.train([
        ((124, 19, 1, 11, 52632.), 16),
        ((87, 15, 1, 10, 48260.), 8),
        ((149, 22, 2, 12, 39816.), 1000),
        ((40, 6, 2, 9, 347.005), 18),
        ((99, 14, 1, 12, 49578), 8),
        ((202, 31, 1, 11, 89862), 15),
        ((115, 18, 1, 12, 73494), 7),
        ((79, 14, 2, 8, 15029), 16),
        ((74, 11, 2, 13, 24056), 6),
        ((30, 6, 1, 8, 68083), 2),
        ((178, 30, 1, 12, 183499), 10),
        ((131, 17, 1, 11, 73951), 12),
        ((154, 21, 1, 12, 42253), 15),
        ((133, 20, 1, 12, 73950), 11),
        ((131, 19, 2, 10, 47346), 10),
        ((50, 7, 4, 9, 3111), 10),
        ((125, 17, 1, 16, 25099), 12),
        ((26, 5, 1, 10, 41676), 4)
    ])
    net.save_to_file('Data/net.xml')


if __name__ == "__main__":
    main()
