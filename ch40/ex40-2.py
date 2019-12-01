# 메타클래스 vs 클래스 데코레이터: 라운드 1

def extra(self, arg): ...

def extras(Class):
    if required():
        Class.extra = extra
    return Class

class Client1: ...
Client1 = extras(Client1)

class Client2: ...
Client2 = extras(Client2)

class Client3: ...
Client3 = extras(Client3)

X = Client1()
X.extra()


def extra(self, arg): ...

def extras(Class):
    if required():
        Class.extra = extra
    return Class

@extras
class Client1: ...                      # Client1 = extras(Cinet1)

@extras
class Client2: ...                      # 인스턴스와 상관없이 클래스를 재결합

@extras
class Client3: ...

X = Clinet1()                   # 보안된 클래스의 인스턴스 생성
X.extra()                       # X는 원래 Client1의 인스턴스
