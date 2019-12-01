# 메타클래스는 타입의 서브클래스

# class문 프로토콜

class = type(classname, superclasses, attributedict)


type.__new__(typeclass, classname, superclasses, attributedict)
type.__init__(class, classname, superclasses, attributedict)


class Eggs: ...                         # 여기에 상속되는 이름

class Spam(Eggs):                       # Eggs로부터 상속
    data = 1                            # 클래스 데이터 속성
    def meth(self, arg):                # 클래스 메서드 속성
        return self.data + arg


Spam = type('Spam', (Eggs,), {'data': 1, 'meth': meth, '__module__': '__main__'})


x = type('Spam', (), {'data': 1, 'meth': (lambda x, y: x.data + y)})
i = x()
x, i
# (<class '__main__.Spam'>, <__main__.Spam object at 0x7f85a6d66cc0>)
i.data, i.meth(2)
# (1, 3)


x.__bases__
# (<class 'object'>,)
[(a, v) for (a, v) in x.__dict__.items() if not a.startswith('__')]
# [('data', 1), ('meth', <function <lambda> at 0x7f85aa5f87b8>)]
