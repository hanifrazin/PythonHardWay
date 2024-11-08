def print_data(**data):
    print(f"type: {type(data)}")
    print(f"data: {data}")

    for key in data:
        print(f"param: {key}, value: {data[key]}")

print_data(phone='nokia 3310',discontinue=False,year=2000,networks=["GSM","CDMA"])

print("\nKombinasi positional argument dan kwargs")
def print_data_comb(message, number, **data):
    print(f"message: {message}")
    print(f"number: {number}")
    print()
    for key in data:
        print(f"param: {key}, value: {data[key]}")

print_data_comb("sesuk prei",2023, phone='samsung galaxy s24',networks=["GSM","CDMA"])

print("\nKombinasi positional argument, args dan kwargs")
def print_data_args_kwargs(message, *params, **others):
    print(f"message: {message}")
    print(f"params: {params}")
    print(f"others: {others}")

print_data_args_kwargs('hello world',1,True,("yesn't","nope"),phone='nokia 3310',discontinue=False,year=2000,networks=["GSM","CDMA"])