# 분수와 소수의 수치 정밀도

a = 1 / 3.0                     # 정밀도는 부동 소수점 하드웨어에 의해 결정됨
b = 4 / 6.0                     # 많은 계산을 통해 정밀도가 손실될 수 있음
a
# 0.3333333333333333
b
# 0.6666666666666666

a + b
# 1.0
a - b
# -0.3333333333333333
a * b
0.2222222222222222


0.1 + 0.1 + 0.1 - 0.3           # 결과는 0이어야 함(0에 가깝긴 하지만 정확하지 않음)
# 5.551115123125783e-17

from fractions import Fraction
Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
# Fraction(0, 1)

from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')


1 / 3                           # 파이썬 2.X에서 트루 나누기를 하려면 '.0' 사용
# 0.3333333333333333

Fraction(1, 3)                  # 수치 정밀도, 두 가지 방법
# Fraction(1, 3)

import decimal
decimal.getcontext().prec = 2
Decimal(1) / Decimal(3)
# Decimal('0.33')


(1 / 3) + (6 / 12)              # 파이썬 2.X에서 트루 나누기를 하려면 '.0' 사용
# 0.8333333333333333

Fraction(6, 12)                 # 자동으로 단순화
# Fraction(1, 2)

Fraction(1, 3) + Fraction(6, 12)
# Fraction(5, 6)

decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12))
# Decimal('0.83')

1000.0 / 1234567890
# 8.100000073710001e-07
Fraction(1000, 1234567890)      # 실험적으로 단순화됨
# Fraction(100, 123456789)
