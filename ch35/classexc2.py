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
