# 예제: 속성을 상속의 원천에 매핑하기

"""
파일 mapattrs.py(3.X + 2.X)

주요 도구: mapattrs()는 인스턴스에 의해 상속되거나 인스턴스에 있는 모든 속성들을
그 속성들이 상속된 클래스나 인스턴스에 매핑함

dir()은 인스턴스의 모든 속성을 제공하는 것으로 가정함
상속을 시뮬레이션하기 위해 새 형식 클래스(그리고 3.X의 모든 클래스)의 검색 순서를 제공하는 클래스의
MRO 튜플이나 2.X의 고전 클래스가 갖는 DFLR 순서를 뜻하는 재귀적 모형을 사용함

또한 여기에서 inheritance()는 버전에 중립적인 클래스 순서를 제공함
이는 3.X/2.7 컴프리헨션을 사용하는 딕셔너리 도구로 분류됨
"""

import pprint
def trace(X, label='', end='\n'):
    print(label + pprint.pformat(X) + end)    # 멋지게 출력하기

def filterdictvals(D, V):
    """
    값 V를 갖는 엔트리가 제거된 딕셔너리 D
    filterdictvals(dict(a=1, b=2, c=1), 1) => {'b': 2}
    """
    return {K: V2 for (K, V2) in D.items() if V2 != V}


def invertdict(D):
    """
    키로 변경된 값을 갖는 딕셔너리 D(값 기준으로 그룹핑함)
    값들은 모두 딕셔너리와 집합의 키 역할을 할 수 있도록 해싱이 가능해야 함
    invertdict(dict(a=1, b=2, c=1)) => {1:['a', 'c'], 2:['b']}
    """
    def keysof(V):
        return sorted(K for K in D.keys() if D[K] == V)
    return {V: keysof(V) for V in set(D.values())}

def dflr(cls):
    """
    cls 지점에서 클래스 트리의 전통적인 깊이 우선. 왼쪽에서 오른쪽 순서
    반복은 불가능함: 파이썬에서 __bases__를 변경할 수 없음
    """
    here = [cls]
    for sup in cls.__bases__:
        here += dflr(sup)
    return here

def inheritance(instance):
    """
    상속 순서 시퀀스: 새로운 형식(MRO) 또는 고전 형식(DFLR)
    """
    if hasattr(instance.__class__, '__mro__'):
        return (instance,) + instance.__class__.__mro__
    else:
        return [instance] + dflr(instance.__class__)

def mapattrs(instance, withobject=False, bysource=False):
    """
    인스턴스의 모든 상속받은 속성을 제공하는 키와
    각 속성의 상속받은 근원인 객체를 제공하는 값으로 이루어진 딕셔너리
    withobject: False= 내장된 클래스 속성 객체 제거
    bysource: True= 속성 대신 객체에 의한 결과를 그룹화
    인스턴스에서 __dict__를 배제하는 슬롯으로 클래스를 지원함
    """
    attr2obj = {}
    inherits = inheritance(instance)
    for attr in dir(instance):
        for obj in inherits:
            if hasattr(obj, '__dict__') and attr in obj.__dict__:    # 슬롯을 참조
                attr2obj[attr] = obj
                break

    if not withobject:
        attr2obj = filterdictvals(attr2obj, object)
    return attr2obj if not bysource else invertdict(attr2obj)

if __name__ == '__main__':
    print('Classic classes in 2.X, new-style in 3.X')
    class A:         attr1 = 1
    class B(A):      attr2 = 2
    class C(A):      attr1 = 3
    class D(B, C):   pass
    I = D()
    print('Py=>%s' % I.attr1)                       # 피이썬의 검색 == 우리가 구현한 검색?
    trace(inheritance(I),             'INH\n')      # [상속 순서]
    trace(mapattrs(I),                'ATTRS\n')    # 속성 => 상속 원천
    trace(mapattrs(I, bysource=True), 'OBJS\n')     # 원천 => [속성]

    print('New-style classes in 2.X and 3.X')
    class A(object): attr1 = 1                      # '(object)' 표기는 3.X에서는 선택 사항임
    class B(A):      attr2 = 2
    class C(A):      attr1 = 3
    class D(B, C):   pass
    I = D()
    print('Py=>%s' % I.attr1)
    trace(inheritance(I),             'INH\n')
    trace(mapattrs(I),                'ATTRS\n')
    trace(mapattrs(I, bysource=True), 'OBJS\n')


# py -2 mapattrs.py 
# 2.X에서는 고전 형식의 클래스, 3.X에서는 새 형식 클래스
# Py=>1
# INH
# [<__main__.D instance at 0x7f3609cc0710>,
#  <class __main__.D at 0x7f3609ca2ae0>,
#  <class __main__.B at 0x7f3609ca2a10>,
#  <class __main__.A at 0x7f3609ca29a8>,
#  <class __main__.C at 0x7f3609ca2a78>,
#  <class __main__.A at 0x7f3609ca29a8>]

# ATTRS
# {'__doc__': <class __main__.D at 0x7f3609ca2ae0>,
#  '__module__': <class __main__.D at 0x7f3609ca2ae0>,
#  'attr1': <class __main__.A at 0x7f3609ca29a8>,
#  'attr2': <class __main__.B at 0x7f3609ca2a10>}

# OBJS
# {<class __main__.A at 0x7f3609ca29a8>: ['attr1'],
#  <class __main__.B at 0x7f3609ca2a10>: ['attr2'],
#  <class __main__.D at 0x7f3609ca2ae0>: ['__doc__', '__module__']}

# 2.X와 3.X에서 새 형식 클래스
# Py=>3
# INH
# (<__main__.D object at 0x7f3609cb9b50>,
#  <class '__main__.D'>,
#  <class '__main__.B'>,
#  <class '__main__.C'>,
#  <class '__main__.A'>,
#  <type 'object'>)

# ATTRS
# {'__dict__': <class '__main__.A'>,
#  '__doc__': <class '__main__.D'>,
#  '__module__': <class '__main__.D'>,
#  '__weakref__': <class '__main__.A'>,
#  'attr1': <class '__main__.C'>,
#  'attr2': <class '__main__.B'>}

# OBJS
# {<class '__main__.C'>: ['attr1'],
#  <class '__main__.D'>: ['__doc__', '__module__'],
#  <class '__main__.A'>: ['__dict__', '__weakref__'],
#  <class '__main__.B'>: ['attr2']}


# py -3
from mapattrs import trace, dflr, inheritance, mapattrs
from testmixin0 import Sub
I = Sub()                       # Sub는 Super와 ListInstance 루트로부터 상속받음
trace(dflr(I.__class__))        # 2.X 검색 순서: lister 전에 암묵적 object!
# [<class 'testmixin0.Sub'>,
#  <class 'testmixin0.Super'>,
#  <class 'object'>,
#  <class 'listinstance.ListInstance'>,
#  <class 'object'>]

trace(inheritance(I))           # 3.X(+ 2.X 새로운 형식) 검색 순서: lister 먼저
# (<testmixin0.Sub object at 0x7f498137d080>,
#  <class 'testmixin0.Sub'>,
#  <class 'testmixin0.Super'>,
#  <class 'listinstance.ListInstance'>,
#  <class 'object'>)

trace(mapattrs(I))
# {'_ListInstance__attrnames': <class 'listinstance.ListInstance'>,
#  '__dict__': <class 'testmixin0.Super'>,
#  '__doc__': <class 'testmixin0.Sub'>,
#  '__init__': <class 'testmixin0.Sub'>,
#  '__module__': <class 'testmixin0.Sub'>,
#  '__str__': <class 'listinstance.ListInstance'>,
#  '__weakref__': <class 'testmixin0.Super'>,
#  'data1': <testmixin0.Sub object at 0x7f498137d080>,
#  'data2': <testmixin0.Sub object at 0x7f498137d080>,
#  'data3': <testmixin0.Sub object at 0x7f498137d080>,
#  'ham': <class 'testmixin0.Super'>,
#  'spam': <class 'testmixin0.Sub'>}

trace(mapattrs(I, bysource=True))
# {<testmixin0.Sub object at 0x7f498137d080>: ['data1', 'data2', 'data3'],
#  <class 'testmixin0.Super'>: ['__dict__', '__weakref__', 'ham'],
#  <class 'testmixin0.Sub'>: ['__doc__', '__init__', '__module__', 'spam'],
#  <class 'listinstance.ListInstance'>: ['_ListInstance__attrnames', '__str__']}

trace(mapattrs(I, withobject=True))
# {'_ListInstance__attrnames': <class 'listinstance.ListInstance'>,
#  '__class__': <class 'object'>,
#  '__delattr__': <class 'object'>,
#  ...등등...


amap = mapattrs(I, withobject=True, bysource=True)
trace(amap)
# {<testmixin0.Sub object at 0x7f498137d080>: ['data1', 'data2', 'data3'],
#  <class 'object'>: ['__class__',
#                     '__delattr__',
#                     ...등등...
#                     '__sizeof__',
#                     '__subclasshook__'],
#  <class 'testmixin0.Super'>: ['__dict__', '__weakref__', 'ham'],
#  <class 'testmixin0.Sub'>: ['__doc__', '__init__', '__module__', 'spam'],
#  <class 'listinstance.ListInstance'>: ['_ListInstance__attrnames', '__str__']}


# mapattrs-slots.py 파일: __slots__ 속성 상속을 테스트
from mapattrs import mapattrs, trace

class A(object): __slots__ = ['a', 'b']; x = 1; y = 2
class B(A):      __slots__ = ['b', 'c']
class C(A):      x = 2
class D(B, C):
    z = 3
    def __init__(self): self.name = 'Bob';

I = D()
trace(mapattrs(I, bysource=True))    # trace(mapattrs(I)와 동일함


# py -3 mapattrs-slots.py 
# {<__main__.D object at 0x7f50033b1e08>: ['name'],
#  <class '__main__.B'>: ['__slots__', 'b', 'c'],
#  <class '__main__.A'>: ['a', 'y'],
#  <class '__main__.C'>: ['x'],
#  <class '__main__.D'>: ['__dict__',
#                         '__doc__',
#                         '__init__',
#                         '__module__',
#                         '__weakref__',
#                         'z']}
