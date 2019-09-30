# 범위와 try except 변수

# py -2
try:
    1 / 0
except Exception as X:          # 2.X 버전에서는 X가 except절에만 한정되지 않음
    print X

# integer division or modulo by zero
X
# ZeroDivisionError('integer division or modulo by zero',)


try:
    1 / 0
except Exception, X:
    print X

# integer division or modulo by zero
X
# ZeroDivisionError('integer division or modulo by zero',)


# py -3
try:
    1 / 0
except Exception, X:
# SyntaxError: invalid syntax

try:
    1 / 0
except Exception as X:          # 3.X에서는 'as' 이름을 except 블록 범위로 한정함
    print(X)

# division by zero
X
# NameError: name 'X' is not defined


X = 99
try:
    1 / 0
except Exception as X:    # 3.X에서는 변수 범위가 한정되며, 블록을 나갈 때 제거됨
    print(X)

# division by zero
X
# NameError: name 'X' is not defined

X = 99
{X for X in 'spam'}    # 2.X/3.X에서 컴프리헨션 표현식 변수는 범위가 한정되긴 하지만 제거되지 않음
# {'m', 'a', 'p', 's'}
X
# 99


try:
    1 / 0
except Exception as X:          # 이 참조는 파이썬에 의해 제거됨
    print(X)
    Saveit = X                  # 예외 인스턴스를 Saveit 변수에 할당하여 참조를 유지

# division by zero
X
# NameError: name 'X' is not defined
Saveit
# ZeroDivisionError('division by zero',)
