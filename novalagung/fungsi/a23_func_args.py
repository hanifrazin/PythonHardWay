def sum_then_print(*numbers):
    total = 0
    for n in numbers:
        total = total + n
    print(total)


sum_then_print(2, 3, 4, 5, 4, 3, 2, 1)

print("\nArgs untuk argument dengan tipe data bervariasi")


def print_data(*params):
    print(f"type: {type(params)}, data: {params}")
    for i in range(len(params)):
        print(f"param {i}: {params[i]}")


print_data("hello python", 123, [5, True, ("yesn't")], {'iwak', 'peyek'})

print("\nKombinasi positional argument dan args")


def sum_then_print_comb(message, *numbers):
    total = 0
    for n in numbers:
        total = total + n
    print(f"{message} {total}")


sum_then_print_comb("total nilai:", 2, 3, 4, 5, 8, 20, 200)

print("\nKombinasi positional argument, args, dan keyword argument")


def sum_then_print_comb_all(message, *numbers, suffix_message):
    total = 0
    for n in numbers:
        total = total + n
    print(f"{message} {total} {suffix_message}")


sum_then_print_comb_all("total nilai:", 2, 3, 4, 5, 8, 20, 200, suffix_message="selesai")
