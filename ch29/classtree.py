# -*- coding: utf-8 -*-
#!python
"""
classtree.py: 네임스페이스 링크를 이용해 인스턴스 트리를 거슬러 올라가며,
상위의 슈퍼클래스를 클릭함. 들여쓰기를 이용해 높이를 표시
"""

def classtree(cls, indent):
    print('.' * indent + cls.__name__)  # 여기에서 클래스 이름을 출력
    for supercls in cls.__bases__:      # 슈퍼클래스로 재귀
        classtree(supercls, indent+3)   # 슈퍼클래스를 한 번 이상 방문할 수도 있음

def instancetree(inst):
    print('Tree of %s' % inst)          # 인스턴스를 표시한다
    classtree(inst.__class__, 3)        # 인스턴스의 클래스로 올라간다

def selftest():
    class A:      pass
    class B(A):   pass
    class C(A):   pass
    class D(B,C): pass
    class E:      pass
    class F(D,E): pass
    instancetree(B())
    instancetree(F())

if __name__ == '__main__': selftest()
