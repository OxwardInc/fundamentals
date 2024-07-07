import decimal
from decimal import Decimal

print(decimal.getcontext())

ctx = decimal.getcontext()
ctx.prec = 5
print(decimal.getcontext())

ctx.prec = 6
print(decimal.getcontext())

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print(decimal.getcontext())

d1 - Decimal('123.4567890')
print(repr(d1))



