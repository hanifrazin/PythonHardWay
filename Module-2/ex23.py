fruit = [
    ['Apples',12,'AAA'],
    ['Oranges',1,'B'],
    ['Pears',2,'A'],
    ['Grapes',14,'UR']
]

cars = [
    ['Cadillac', ['Black','Big',34500]],
    ['Corvette', ['Red','Little',1000000]],
    ['Ford', ['Blue','Medium',1234]],
    ['BMW', ['White','Baby',7890]]
]

languages = [
    ['Python',['Slow',['Terrible','Mush']]],
    ['JavaScript',['Moderate',['Alright','Bisarre']]],
    ['Perl6',['Moderate',['Fun','World']]],
    ['C',['Fast',['Annoying','Dangerous']]],
    ['Forth',['Fast',['Fun','Difficult']]]
]

print("\nFruit Challenge")
print(fruit[0][1]) # 12
print(fruit[0][2]) # AAA
print(fruit[2][1]) # 2
print(fruit[1][0]) # Oranges
print(fruit[3][0]) # Grapes
print(fruit[3][1]) # 14
print(fruit[0][0]) # Apples

print("\nCars Challenge")
print(cars[0][1][1]) # Big
print(cars[1][1][0]) # Red
print(cars[2][1][2]) # 1234
print(cars[3][1][0]) # White
print(cars[3][1][2]) # 7890
print(cars[0][1][0]) # Black
print(cars[0][1][2]) # 34500
print(cars[2][1][0]) # Blue

print("\nLanguage Challenge")
print(languages[0][1][0]) # Slow
print(languages[1][1][1][0]) # Alright
print(languages[3][1][1][1]) # Dangerous
print(languages[3][1][0]) # Fast
print(languages[4][1][1][1]) # Difficult
print(languages[4][1][1][0]) # Fun
print(languages[3][1][1][0]) # Annoying
print(languages[1][1][0]) # Moderate
# print(languages[][][][]) # Weird
