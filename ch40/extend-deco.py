# 데코레이터로 확장: 메타클래스의 __init__이 제공하는 것과 동일

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

def Extender(aClass):
    aClass.eggs = eggsfunc              # 인스턴스가 아니라 클래스를 관리
    aClass.ham  = hamfunc               # 메타클래스의 __init__과 동일
    return aClass

@Extender
class Client1:                          # Client1 = Extender(Clinet1)
    def __init__(self, value):          # class문 마자막에서 재결합
        self.value = value
    def spam(self):
        return self.value * 2

@Extender
class Client2:
    value = 'ni?'

X = Client1('Ni')                       # X는 Client1의 인스턴스
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))
