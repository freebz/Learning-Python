# -*- coding: utf-8 -*-
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
