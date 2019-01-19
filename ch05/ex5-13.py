# 다른 숫자 타입

# 소수 타입

# 소수의 기초

0.1 + 0.1 + 0.1 - 0.3           # 파이썬 3.6
# 5.551115123125783e-17


print(0.1 + 0.1 + 0.1 - 0.3)    # 이전 버전 파이썬에서 결과 (3.6과 다름)
# 5.551115123125783e-17


from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
# Decimal('0.0')


Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30')
# Decimal('0.00')


Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)
# Decimal('2.775557561565156540423631668E-17')
