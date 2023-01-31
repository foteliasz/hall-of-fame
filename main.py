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

def fromAndrzej():
    print("Tomek, thanks for cooperation!!, in particular ...", end='')
    input()
    print("... for fighting together with legacy code (de-authorization, Keycloak config, Python scripts, workarounds etc.)", end='')
    input()
    print("... for designing new stuff (client self service, thread modeling, security vulnerabilities, helm charts etc.)", end='')
    input()
    print("... and dready culmination related to Kerberos :D")
    input()
    print("and what more important for a few very good meetings in real :)")
    print("All the best to You!!!")
    
def fromSebb():
    print("Kuba, thank you very much for all you have done for us!")
    print("It was a real pleasure working with you.")
    print("Good luck and hopefully see you next time.")

gabiFunc = Func("from-gabi", "Gabriela Chacuś", fromGabi)
olaFunc = Func("from-ola", "Aleksandra Dura", fromOla)
wotoFunc = Func("check-weather", "Wojciech Tomaszek", checkWeather)
agaFunc = Func("from-aga", "Agnieszka Kominek", fromAga)
andFunc = Func("from-andrzej", "Andrzej Martyna", fromAndrzej)
fromSebb = Func("from-Sebb", "Sebastian Malinowski", fromSebb)

functions = [
    Func("hej", "jakub", lambda: print("wszystkiego dobrego i do zobaczenia")),
    gabiFunc,
    wotoFunc,
    agaFunc,
    olaFunc,
    andFunc,
    fromSebb
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
    input()
