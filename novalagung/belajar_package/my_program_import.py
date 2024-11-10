a = 10
b = 15

import libs.calculate as calc
import libs.common.number as num
import libs.common.message as msg

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
print(num.note)
print(msg.note)

res = calc.calc_hypotenuse(a,b)
msg.print_hypotenuse(res)

res = num.sqrt(a**2 + b**2)
msg.print_hypotenuse(res)

res = num.sqrt(num.pow(a) + num.pow(b))
msg.print_hypotenuse(res)