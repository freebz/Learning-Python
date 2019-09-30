# 통합된 try문의 구문

try -> except -> else -> finally


try:                            # 형식 1
    statements
except [type [as value]]:       # 파이썬 2.X에서는 [type [,value]]
    statements
[except [type [as value]]:
    statements]*
[else:
    statements]
[finally:
    statements]

try:                            # 형식 2
    statements
finally:
    statements
