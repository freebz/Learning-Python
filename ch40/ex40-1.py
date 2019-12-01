# '헬퍼(Helper)' 함수의 단점

class Extras:
    def extra(self, args):              # 일반적인 상속: 너무 정적인 방식
        ...
        
class Client1(Extras): ...              # 클라이언트는 extra 메서드를 상속받음
class Client2(Extras): ...
class Client3(Extras): ...

X = Client1()                           # 인스턴스를 생성
X.extra()                               # extra 메서드 실행


def extra(self, arg): ...

class Client1: ...                      # 클라이언트 보안: 너무 분산됨
if required():
    Client1.extra = extra

class Client2: ...
if required():
    Client2.extra = extra

class Client3: ...
if required():
    Client3.extra = extra

X = Client1()
x.extra()


def extra (self, arg): ...

def extras(Class):                      # 관리자 함수: 너무 수동적임
    if required():
        Class.extra = extra

class Client1: ...
extras(Client1)

class Client2: ...
extras(Client2)

class Client3: ...
extras(Client3)

X = Client1()
X.extra()


def extra(self, arg): ...

class Extras(type):
    def __init__(Class, classname, superclasses, attributedict):
        if required():
            Class.extra = extra

class Client1(metaclass=Extras): ...    # 메타클래스 선언만(3.X 형태)
class Client2(metaclass=Extras): ...    # 클라이언트 클래스는 메타클래스의 인스턴스
class Client3(metaclass=Extras): ...

X = Client1()                           # X는 Client1의 인스턴스
X.extra()
