command = input("Enter command: ")

match command.split(' '):

    case["greet"]:
        name = input("Your name: ")
        print("hello", name)

    case["greet", "thrall"]:
        print("hello noval, how is the horde?")

    case["greet", *args]:
        print("hello", ' '.join(args))

    case["sum_numbers"]:
        numbers = input("The numbers separated by space: ")
        total = 0
        for str in numbers.split(' '):
            total = total + int(str)
        print("total:", total)

    case["sum_numbers", *args]:
        total = 0
        for str in args:
            total = total + int(str)
        print("total:", total)

    case _:
        print("unrecognized command")