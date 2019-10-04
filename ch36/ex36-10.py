# 에러와 역추적 결과를 표시하기

import traceback

def inverse(x):
    return 1 / x

try:
    inverse(0)
except Exception:
    traceback.print_exc(file=open('badly.exc', 'w'))
print('Bye')


# python badly.py 
# Bye

# type badly.exc
# Traceback (most recent call last):
#   File "badly.py", line 7, in <module>
#     inverse(0)
#   File "badly.py", line 4, in inverse
#     return 1 / x
# ZeroDivisionError: integer division or modulo by zero
