# 다중 상속: 순서가 중요

class ListTree:
    def __str__(self): ...

class Super:
    def __str__(self): ...

class Sub(ListTree, Super):     # ListTree를 먼저 나열하여 ListTree의 __str__를 가져옴

x = Sub()                       # 상속은 Super 전에 ListTree를 검색


class ListTree:
    def __str__(self): ...
    def other(self): ...

class Super:
    def __str__(self): ...
    def other(self): ...

class Sub(ListTree, Super):     # ListTree를 먼저 두어, ListTree의 __str__ 선택
    other = Super.other         # 하지만 other는 Super의 버전을 명시적으로 선택
    def __init__(self):
        ...

x = Sub()                       # 상속은 Sub를 ListTree/Super 전에 검색


class Sub(Super, ListTree):     # Super의 other를 순서에 의해 가짐
    __str__ = Lister.__str__    # 명시적으로 Lister.__str__을 선택
