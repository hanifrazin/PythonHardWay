command = input("Enter command: ")

match command.split(' '):

    case ["greet"]:
        name = input("Your name: ")
        print("hello", name)

    case ["greet", "thrall"]:
        print("hello noval, how is the horde?")

    case ["greet", name, ("morning" | "afternoon" | "evening") as t]:
        print("hello",name,"good",t)

    case ["greet", name] | ["hello", name]:
        print("hello",name)

    case ([other] | other) as o:
        print(f"command {o} is not recognized")