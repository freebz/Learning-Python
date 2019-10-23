# 예제: 속성 검증

# 프로퍼티를 이용한 검증

# validate_properties.py 파일

class CardHolder(object):               # 2.X에서는 "(object)"를 필요로 함
    acctlen = 8                         # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                    # 인스턴스 데이터
        self.name = name                    # 프로퍼티 setter 도구를 호출
        self.age  = age                     # __X는 클래스 이름을 포함하여 맹글링됨
        self.addr = addr                    # addr은 관리되지 않음
                                            # remain은 데이터가 없음

    def getName(self):
        return self.__name
    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value
    name = property(getName, setName)

    def getAge(self):
        return self.__age
    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value
    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'
    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invalid acct number')
        else:
            self.__acct = value
    acct = property(getAcct, setAcct)

    def remainGet(self):                    # 이미 속성으로 사용되고 있지 않다면
        return self.retireage - self.age    # 메서드가 아니라 속성일 수도 있음
    remain = property(remainGet)


# validate_tester.py 파일
from __future__ import print_function    # 2.X

def loadclass():
    import sys, importlib
    modulename = sys.argv[1]                        # 명령줄에 모듈 이름이 있음
    module = importlib.import_module(modulename)    # 이름 문자열로 모듈 임포트
    print('[Using: %s]' % module.CardHolder)        # getattr() 호출 필요 없음
    return module.CardHolder

def printholder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')

if __name__ == '__main__':
    CardHolder = loadclass()
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    printholder(bob)
    bob.name = 'Bob Q. Smith'
    bob.age  = 50
    bob.acct = '23-45-67-89'
    printholder(bob)

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    printholder(sue)
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')

    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")

    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')


# py -3 validate_tester.py validate_properties
# [Using: <class 'validate_properties.CardHolder'>]
# 12345*** / bob_smith / 40 / 19.5 / 123 main st
# 23456*** / bob_q._smith / 50 / 9.5 / 123 main st
# 56781*** / sue_jones / 35 / 24.5 / 124 main st
# Bad age for Sue
# Can't set sue.remain
# Bad acct for Sue
