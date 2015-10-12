from threading import Timer
from anybar import AnyBar

choose = input("What are you making? (tea or coffee):\n>> ").lower()


def tea():
    AnyBar().change('red', text="Tea ready!")


def coffee():
    AnyBar().change('purple', text="Coffee ready!")

option1 = Timer(2 * 60, tea)

option2 = Timer(4 * 60, coffee)

if choose == "tea":
    option1.start()
elif choose == "coffee":
    option2.start()
else:
    print("Invalid input")







