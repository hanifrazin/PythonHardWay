sample_list = [2, 3, 4]
is_3_exists = 3 in sample_list
print(f"Is 3 exist? {is_3_exists}")
# output -> True

sample_tuple = ("hello","python")
is_hello_exists = "hello" in sample_tuple
print(f"Is hello exist? {is_hello_exists}")

sample_dict = { "nama": "hanif","age": 29 }
is_key_nama_exists = "nama" in sample_dict
print(f"Is key nama exist? {is_key_nama_exists}")

sample_set = { "sesuk", "preiiii" }
is_prei = "preiiii" in sample_set
print(f"Is preiiii exist? {is_prei}")

text = 'Hello World'
is_substring_exists = 'orl' in text
print(f"Is substring exists? {is_substring_exists}")