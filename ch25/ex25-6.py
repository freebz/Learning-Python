# 통화 기호: 유니코드 실제 사례

from __future__ import print_function # 2.X에서 print를 함수로 사용
from formats import money
X = 54321.987

print(money(X), money(X, 0, ''))
print(money(X, currency=u'\xA3'), money(X, currency=u'\u00A5'))
print(money(X, currency=b'\xA3'.decode('latin-1')))

print(money(X, currency=u'\u20AC'), money(X, 0, b'\xA4'.decode('iso-8859-15')))
print(money(X, currency=b'\xA4'.decode('latin-1')))


# $54,321.99 54,321.99
# £54,321.99 ¥54,321.99
# £54,321.99
# €54,321.99 €54,321.99
# ¤54,321.99
