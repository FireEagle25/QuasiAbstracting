from Abstractor.Abstractor import Abstractor

with open("text.txt", "r") as f:
    text = f.read()
    prescinder = Abstractor(text)
    prescinder.truncate(0.5)
    prescinder.truncate(0.1)