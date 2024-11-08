def get_full_name1(first_name, last_name):
    return f"{first_name} {last_name}"

get_full_name2 = lambda first_name, last_name : f"{first_name} {last_name}"

res = get_full_name1("Hanif","Razin")
print(res)

res = get_full_name2("Nizar","Rahmatullah")
print(res)

get_full_name3 = lambda first_name, last_name = "" : f"{first_name} {last_name}".strip()
res = get_full_name3("Thrall")
print(res)

res = get_full_name3(first_name="Farai",last_name="Nadjar")
print(res)