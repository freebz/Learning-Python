# -*- coding: utf-8 -*-
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
