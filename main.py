import sys

from Core.Abstractors.Implementations.NeuralNetAbstractor import NeuralNetAbstractor
from Core.Abstractors.Implementations.StatisticAbstractor import StatisticAbstractor


def main():

    if len(sys.argv) < 3:
        print("Первым аргументом введите имя файла, "
              "вторым - тип реферирования(1 - с помощью статистического метода, 2 - с помощью нейронных сетей), "
              "третьим аргументом нужно указать процент как вещ. число для сокращения файла.")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as f:
            text = f.read()
            abstractor = StatisticAbstractor(text) if sys.argv[2] == "1" else NeuralNetAbstractor(text, 'Data/net.xml')
            abstractor.truncate(float(sys.argv[3]))
    except FileNotFoundError:
        print('Файл с текстом не найден')

    exit()


if __name__ == "__main__":
    main()