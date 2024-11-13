command = input("Enter command: ")

match command:

    case "greet":
        name = input("Your name: ")
        print(f"Hello {name}")

    case "sum_numbers":
        numbers = input("The numbers separated by space: ")
        total = 0
        print(numbers.split(' '))
        for str in numbers.split(' '):
            total = total + int(str)
        print(f"The total is {total}")

    case "luck_number":
        import random
        n = random.randint(0,100)
        print(f"The lucky number is: {n}")

    case _:
        print("unrecognized command")