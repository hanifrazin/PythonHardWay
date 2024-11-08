def aggregate(message, numbers, f):
    res = f(numbers)
    print(f"{message} is {res}")

def sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def avg(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

aggregate("total", [24,67,22,98,3,50],sum)
aggregate("avg", [24,67,22,98,3,50],avg)
aggregate("max numbers", [24,67,22,98,3,50],max)
aggregate("min numbers", [24,67,22,98,3,50],min)