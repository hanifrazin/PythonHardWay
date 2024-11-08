def get_hello_message():
    return "hello python"

res = get_hello_message()
print(res)

get_hello_message2 = lambda : "hello python"

res = get_hello_message2()
print(res)