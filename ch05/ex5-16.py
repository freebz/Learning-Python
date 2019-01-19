# 분수 타입

# 분수의 기초

from fractions import Fraction
x = Fraction(1, 3)              # 분자, 분모
y = Fraction(4, 6)              # gcd(최대공약수 함수)에 의해 2,3 으로 단순화됨

x
# Fraction(1, 3)
y
# Fraction(2, 3)
print(y)
# 2/3


x + y
# Fraction(1, 1)
x - y                           # 정확한 결과가 나옴(분자, 분모)
# Fraction(-1, 3)
x * y
# Fraction(2, 9)


Fraction('.25')
# Fraction(1, 4)
Fraction('1.25')
# Fraction(5, 4)

Fraction('.25') + Fraction('1.25')
# Fraction(3, 2)
