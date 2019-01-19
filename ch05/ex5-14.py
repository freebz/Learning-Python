# 소수 정밀도를 전역으로 설정하기

import decimal
decimal.Decimal(1) / decimal.Decimal(7)
# Decimal('0.1428571428571428571428571429')                  # 기본: 28 자리

decimal.getcontext().prec = 4
decimal.Decimal(1) / decimal.Decimal(7)
# Decimal('0.1429')                                          # 고정된 정밀도

Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)    # 0에 근접
# Decimal('1.110E-17')


1999 + 1.33                     # 3.6에서 출력되는 것 다보메모리상에 더 많은 자릿수를 가지고 있음
# 2000.33

decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))
pay
# Decimal('2000.33')
