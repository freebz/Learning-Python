# 유사개별 클래스 속성

# 이름 맹글링 개요

# 왜 유사개별 속성을 사용하는가?

class C1:
    def meth1(self): self.X = 88        # 나는 X는 내 것이라 가정
    def meth2(self): print(self.x)


class C2:
    def metha(self): self.X = 99        # 나도
    def methb(self): print(self.X)


class C3(C1, C2): ...
I = C3()                                # I에 X는 하나만!


class C1:
    def meth1(self): self.__X = 88      # 이제 X는 내거!
    def meth2(self): print(self.__X)    # I에서 _C1__X 로 바뀜
class C2:
    def metha(self): self.__X = 99      # 나도
    def methb(self): print(self.__X)    # I에서 _C2__X 로 바뀜

class C3(C1, C2): pass
I = C3()                                # I 안에 두 개의 이름 X가 존재함

I.meth1(); I.metha()
print(I.__dict__)
I.meth2(); I.methb()


# python pseudoprivate.py
# {'_C1__X': 88, '_C2__X': 99}
# 88
# 99


class Super:
    def method(self): ...                   # 실제 적용 메서드

class Tool:
    def __method(self): ...                 # _Tool__메서드가 됨
    def other(self): self.__method()        # 나의 내부 메서드를 사용

class Sub1(Tool, Super):
    def actions(self): self.method()        # 예상대로 Super.method를 실행

class Sub2(Tool):
    def __init__(self): self.emthod = 99    # Tool.__method를 망치지 않음
