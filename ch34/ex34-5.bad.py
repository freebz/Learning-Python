# 예제: 기본 동작

def gobad(x, y):
    return x / y

def gosouth(x):
    print(gobad(x, 0))

gosouth(1)


# % python bad.py 
# Traceback (most recent call last):
#   File "bad.py", line 7, in <module>
#     gosouth(1)
#   File "bad.py", line 5, in gosouth
#     print(gobad(x, 0))
#   File "bad.py", line 2, in gobad
#     return x / y
# ZeroDivisionError: integer division or modulo by zero
