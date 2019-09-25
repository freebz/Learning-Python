# -*- coding: utf-8 -*-
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
