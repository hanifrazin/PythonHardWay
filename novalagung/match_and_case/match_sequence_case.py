command = input("Enter command: ")
inputs = command.split(' ')

match inputs:

    case ["greet"]:
        name = input("Your name: ")
        print(f"Hello {name}")

    case ["greet","thrall"]:
        print("hello noval, how is the horde?")

    case ["sum_numbers"]:
        numbers = input("The numbers separated by space: ")
        total = 0
        for str in numbers.split(' '):
            total = total + int(str)
        print("total:", total)

    case _:
        print("unrecognized command")
