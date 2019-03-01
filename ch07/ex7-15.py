# 기존 문자열 모듈의 함수들(3.X에서 사리짐)

S = 'a+b+c+'
x = S.replace('+', 'spam')
x
# 'aspambspamcspam'


import string
y = string.replace(S, '+', 'spam')
y
# 'aspambspamcspam'
