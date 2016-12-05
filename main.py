import sys

from Abstractor.Abstractor import Abstractor


def main():

    if len(sys.argv) < 3:
        print("Введите имя файла как аргумент при запуске файла, "
              "а вторым нужно указать процент как вещ. число для сокращения файла.")
        sys.exit(1)

    print("Такс... Тут должна быть проверка на существование файла и блабла. Если кому надо, пусть сам делает.")

    with open(sys.argv[1], "r") as f:
        text = f.read()
        abstractor = Abstractor(text)
        abstractor.truncate(float(sys.argv[2]))

    exit()


if __name__ == "__main__":
    main()