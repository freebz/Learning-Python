# 3.X와 2.X에서 메타클래스 실행

class = Meta(classname, superclasses, attributedict)


Meta.__new__(Meta, classname, superclasses, attributedict)
Meta.__init__(class, classname, superclasses, attributedict)


class Spam(Eggs, metaclass=Meta):       # Eggs로부터 상속, Meta의 인스턴스
    data = 1                            # 클래스 데이터 속성
    def meth(self, arg):                # 클래스 메서드 속성
        return self.data + arg


Spam = Meta('Spam', (Eggs,), {'data': 1, 'meth': meth, '__module--': '__main__'})
