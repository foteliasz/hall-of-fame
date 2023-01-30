class Func:
    def __init__(self, name, author, delegate):
        self.name = name
        self.author = author
        self.delegate = delegate


def fromGabi():
    print("It was a pleasure working with You!")
    print("Fly high and good luck!")

def fromOla():
    print("Goodbye and good luck! It was great to work with you!")


def checkWeather():
    print("There is always good weather for great people! So, YOU do not need to worry :)")
    print("All the best to you!")

def fromAga():
    print("Thank you for being a great teammate!")
    print("All the best on your new adventure!")

gabiFunc = Func("from-gabi", "Gabriela Chacuś", fromGabi)
olaFunc = Func("from-ola", "Aleksandra Dura", fromOla)
wotoFunc = Func("check-weather", "Wojciech Tomaszek", checkWeather)
agaFunc = Func("from-aga", "Agnieszka Kominek", fromAga)

functions = [
    Func("hej", "jakub", lambda: print("wszystkiego dobrego i do zobaczenia")),
    gabiFunc,
    wotoFunc,
    agaFunc,
    olaFunc
]

while True:
    print("Good morning Tomasz!")
    print("List of available functions:")
    for index, function in enumerate(functions):
        print(f'{index + 1}. Function: >{function.name}<, by: {function.author}')

    selection = None
    while selection is None:
        tmp = input("What function would you like to run: ")
        if not tmp.isnumeric():
            continue
        tmp = int(tmp) - 1
        if tmp < 0 or tmp >= len(functions):
            continue
        selection = tmp
    print()
    functions[selection].delegate()
    print()
