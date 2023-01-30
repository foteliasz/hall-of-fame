class Func:
    def __init__(self, name, author, delegate):
        self.name = name
        self.author = author
        self.delegate = delegate


def example():
    print("You are definitely awesome Today ...!")
    print("Keep it up!")


func = Func("example-func", "...", example)

functions = [
    func
]

while True:
    print("Good morning ...")
    print("List of available functions:")
    print(type(functions))
    for index, function in enumerate(functions):
        print(f'{index + 1}. Function: >{function.name}<, by: {function.author}')

    selection = None
    while selection is None:
        tmp = input("What function would you like to run:")
        if not tmp.isnumeric():
            continue
        tmp = int(tmp) - 1
        if tmp < 0 or tmp > len(functions) + 1:
            continue
        selection = tmp
    print()
    functions[selection].delegate()
    print()
