import json
from pprint import pprint

# Menggunakan { }
profile = {
    "id": 2,
    "name": "john wick",
    "hobbies": ["playing with pencil"],
    "is_female": False,
}
pprint(profile)
print(json.dumps(profile, indent=4))

# Menggunakan fungsi dict() dengan isi argument key-value
profiles = dict(
    set="id",
    name="john wick",
    hobbies=["playing with pencil"],
    is_female=False,
)
print("\n")
pprint(profiles)
print(json.dumps(profiles, indent=4))

# Menggunakan fungsi dict() dengan isi list tuple
profiles2 = dict([
    ('set','id'),
    ('name','john wick'),
    ('hobbies',['playing with pencil']),
    ('is_female',False),
])
print("\n")
pprint(profiles2)
print(json.dumps(profiles2, indent=4))