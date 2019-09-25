# 클래스 데코레이터와 메타클래스의 소개

def decorator(aClass): ...

@decorator                      # 클래스 데코레이터 구문
class C: ...


def decorator(aClass): ...
class C: ...                    # 그에 상응하는 이름 재결함
C = decorator(C)


def count(aClass):
    aClass.numInstances = 0
    return aClass               # 래퍼 함수 대신 클래스 자체를 반환

@count
class Spam: ...                 # Spam = count(Spam)와 동일

@count
class Sub(Spam): ...            # numInstances = 0은 여기에서는 불필요

@count
class Other(Spam): ...


@count
def spam(): pass                # spam = count(spam)와 동일

@count
class Other: pass               # Other = count(Other)와 동일

spam.numInstances               # 둘 모두 0으로 설정
Other.numInstances


def decorator(cls):                     # @ decoration 시
    class Proxy:
        def __init__(self, *args):      # 인스턴스 생성 시: cls를 생성
            self.wrapped = cls(*args)
        def __getattr__(self, name):    # 속성 가져올 때: 추가 동작은 여기에
            return getattr(self.wrapped, name)
    return Proxy

@decorator
class C: ...                            # C = decorator(C)와 동일
X = C()                                 # C를 감싸는 프록시 생성, 나중에 X.attr를 잡아냄


class Meta(type):
    def __new__(meta, classname, supers, classdict):
        ...추가 로직 + 타입 호출을 통한 클래스 생성...
class C(metaclass=Meta):
    ... 인스턴스 생성이 Meta로 라우팅...  # C = Meta('C', (), {...})와 동일


class C:
    __metaclass__ = Meta    ...인스턴스 생성이 Meta로 라우팅됨...


classname = Meta(classname, superclasses, attributedict)
