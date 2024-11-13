command = input("Enter command: ")
inputs = command.split(' ')

match inputs:

    case ["greet"]:
        name = input("Your name: ")
        print(f"Hello {name}")

    case ["greet","thrall"]:
        print("hello noval, how is the horde?")

    case ["greet", name]:
        print(f"Hello {name}")

    case _:
        print("unrecognized command")
