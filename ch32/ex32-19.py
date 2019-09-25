# 슬롯의 영향에 대한 예제: ListTree와 mapattrs

class C(ListTree): pass
X = C()                                      # OK: __slots__ 이 사용되지 않음
print(X)

class C(ListTree): __slots__ = ['a', 'b']    # OK: 슈퍼클래스가 __dict__를 생성함
X = C()
X.c = 3
print(X)                                     # X의 c와 C의 a와 b를 디스플레이


class A: __slots__ = ['a']                   # 위의 첫 번째 아이템에 의거, 둘 모두 OK
class B(A, ListTree): pass

class A: __slots__ = ['a']
class B(A, ListTree): __slots__ = ['b']      # B의 b와 A의 a를 디스플레이


def mapattrs(instance, withobject=False, bysource=False):
    for attr in dir(instance):
        for obj in inherits:
            if attr in obj.__dict__:    # 만약 __slots__을 사용한다면 실패할 것임

class C: __slots__ = ['a']
X = C()
mapattrs(X)
# AttributeError: 'C' object has no attribute '__dict__'


    if attr in getattr(obj, '__dict__', {}):

    if hasattr(obj, '__dict__') and attr in obj.__dict__:
