from NeuralNet.NeuralNet import Net


def main():
    net = Net()
    net.train([((1, 2, 3, 4, 5), 10), ((1, 2, 3, 4, 5), 10),((1, 2, 3, 4, 5), 10),((1, 2, 3, 4, 5), 10),((1, 2, 3, 4, 5), 10),((1, 2, 3, 4, 5), 10),((1, 2, 3, 4, 5), 10)])
    net.save_to_file('net.xml')


if __name__ == "__main__":
    main()
