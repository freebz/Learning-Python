# 클래스 기반 예외

# 예외 클래스 코딩하기

class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
    X = General()               # 슈퍼클래스 인스턴스 발생
    raise X

def raiser1():
    X = Specific1()             # 서브클래스 인스턴스 발생
    raise X

def raiser2():
    X = Specific2()             # 다른 버스클래스 인스턴스 발생
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:             # General 또는 어떤 서브클래스라도 매칭
        import sys
        print('caught: %s' % sys.exc_info()[0])

# python classexc.py
# caught: <class '__main__.General'>
# caught: <class '__main__.Specific1'>
# caught: <class '__main__.Specific2'>


class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0(): raise General()
def raiser1(): raise Specific1()
def raiser2(): raise Specific2()

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General as X:                     # X는 발생된 인스턴스
        print('caught: %s' % X.__class__)    # sys.exc_info()[0]과 동일
