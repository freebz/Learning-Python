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
