a = 10
b = 15

from libs import calculate as calc
from libs.common import *

# print(libs.calculate.note)
# print(libs.common.number.note)
# print(libs.common.message.note)
#
# res = libs.calculate.calc_hypotenuse(a,b)
# libs.common.message.print_hypotenuse(res)
#
# res = libs.common.number.sqrt(a**2 + b**2)
# libs.common.message.print_hypotenuse(res)
#
# res = libs.common.number.sqrt(libs.common.number.pow(a) + libs.common.number.pow(b))
# libs.common.message.print_hypotenuse(res)

print(calc.note)
print(number.note)
print(message.note)

res = calc.calc_hypotenuse(a,b)
message.print_hypotenuse(res)

res = number.sqrt(a**2 + b**2)
message.print_hypotenuse(res)

res = number.sqrt(number.pow(a) + number.pow(b))
message.print_hypotenuse(res)