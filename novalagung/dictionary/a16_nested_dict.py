from dict_data import profile

print("name:", profile["name"])
print("hobbies:", profile["hobbies"])
print("affliations:")

for item in profile["affliations"]:
    print(f"{item.get('name')}, {item.get('affliation')}")