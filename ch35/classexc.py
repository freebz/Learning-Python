# -*- coding: utf-8 -*-
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

        
