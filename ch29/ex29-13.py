# 네임스페이스 연결: 트리 등반자

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


# py -2 classtree.py 
# Tree of <__main__.B instance at 0x7f0ee8203ab8>
# ...B
# ......A
# Tree of <__main__.F instance at 0x7f0ee8203ab8>
# ...F
# ......D
# .........B
# ............A
# .........C
# ............A
# ......E


# py -3 classtree.py 
# Tree of <__main__.selftest.<locals>.B object at 0x7f4295ae9a90>
# ...B
# ......A
# .........object
# Tree of <__main__.selftest.<locals>.F object at 0x7f4295ae9a90>
# ...F
# ......D
# .........B
# ............A
# ...............object
# .........C
# ............A
# ...............object
# ......E
# .........object


# c:\python33\python
class Emp: pass

class Person(Emp): pass

bob = Person()

import classtree
classtree.instancetree(bob)
# Tree of <__main__.Person object at 0x7f5bc0029518>
# ...Person
# ......Emp
# .........object
