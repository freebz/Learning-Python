# 내장 예외 범주들

try:
    action()
except Exception:               # 시스템 종료는 여기에서 잡히지 않음
    ...모든 응용 예외 처리...
else:
    ...예외가 아닌 경우 처리...


# py -3.2
try:
    f = open('nonesuch.txt')
except IOError as V:
    if V.errno == 2:            # 또는 errno.N, V.args[0]
        print('No such file')
    else:
        raise                   # 다른 예외들은 전파

# No such file


# py -3.3
try:
    f = open('nonesuch.txt')
except FileNotFoundError:
    print('No such file')

# No such file
