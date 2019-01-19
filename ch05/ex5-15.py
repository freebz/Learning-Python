# 소수 콘텍스트 관리자

import decimal
decimal.Decimal('1.00') / decimal.Decimal('3.00')
# Decimal('0.3333333333333333333333333333')

with decimal.localcontext() as ctx:
    ctx.prec = 2
    decimal.Decimal('1.00') / decimal.Decimal('3.00')

# Decimal('0.33')

decimal.Decimal('1.00') / decimal.Decimal('3.00')
# Decimal('0.3333333333333333333333333333')
