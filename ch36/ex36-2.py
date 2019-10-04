# 예제: 구문적 중첩

try:
    try:
        action2()
    except TypeError:           # 가장 최근의 매칭되는 try문
        print('inner try')
except TypeError:               # 여기, 중첩된 핸들러가 다시 일어날 때만
    print('outer try')


try:
    try:
        raise IndexError
    finally:
        print('spam')
finally:
    print('SPAM')

# spam
# SPAM
# Traceback (most recent call last):
#   File "<stdin>", line 3, in <module>
# IndexError


def raise1(): raise IndexError
def noraise(): return
def raise2(): raise SyntaxError

for func in (raise1, noraise, raise2):
    print('<%s>' % func.__name__)
    try:
        try:
            func()
        except IndexError:
            print('caught IndexError')
    finally:
        print('finally run')
    print('...')


# python except-finally.py 
# <raise1>
# caught IndexError
# finally run
# ...
# <noraise>
# finally run
# ...
# <raise2>
# finally run
# Traceback (most recent call last):
#   File "except-finally.py", line 9, in <module>
#     func()
#   File "except-finally.py", line 3, in raise2
#     def raise2(): raise SyntaxError
# SyntaxError: None
