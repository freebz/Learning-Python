# 디스크립터 메서드 인수

class Descriptor:               # 2.X에서는 "(object)"를 추가
    def __get__(self, instance, owner):
        print(self, instance, owner, sep='\n')

class Subject:                  # 2.X에서는 "(object)"를 추가
    attr = Descriptor()         # 디스크립터 인스턴스는 클래스 속성

X = Subject()
X.attr
# <__main__.Descriptor object at 0x7fa1f8603390>
# <__main__.Subject object at 0x7fa1f8603d68>
# <class '__main__.Subject'>

Subject.attr
# <__main__.Descriptor object at 0x7fa1f8603390>
# None
# <class '__main__.Subject'>


X.attr  ->  Descriptor.__get__(Subject.attr, X, Subject)
