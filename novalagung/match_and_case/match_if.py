command = input("Enter command: ")

match command.split(' '):

    case ["greet"]:
        name = input("Your name: ")
        print("hello", name)

    case ["greet", name] if name == "thrall":
        print("hello noval, how is the horde?")

    case ["greet", name, ("morning" | "afternoon" | "evening") as t]:
        print("hello", name, "good", t)

    case other:
        print(f"command {other} is not defined")
