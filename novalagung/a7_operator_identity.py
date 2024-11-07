num_1 = 100001
num_2 = 100001

res = num_1 is num_2
print("num_1 is num_2 = ",res)
print("id(num_1): %s, id(num_2): %s" % (id(num_1), id(num_2)))
print("message: %s %s %s" % ("hello","python","learner"))
print("message:","hello","python","learner")

data_1 = "hello world"
id_data_1 = id(data_1)

print("data_1:",data_1)
print("id_data_1:",id_data_1)