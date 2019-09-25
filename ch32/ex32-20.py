# 슬롯의 속도는 어떠한가?

# slots-test.py 파일
from __future__ import print_function
import timeit
base = """
Is = []
for i in range(1000):
    X = C()
    X.a = 1; X.b = 2; X.c = 3; X.d = 4
    t = X.a + X.b + X.c + X.d
    Is.append(X)
"""

stmt = """
class C(object):
    __slots__ = ['a', 'b', 'c', 'd']
""" + base
print('Slots =>', end=' ')
print(min(timeit.repeat(stmt, number=1000, repeat=3)))

stmt = """
class C(object):
    pass
""" + base
print('Nonslots=>', end=' ')
print(min(timeit.repeat(stmt, number=1000, repeat=3)))


# py -3 slots-test.py
# Slots    => 0.7780903942045899
# Nonslots => 0.9888108080898417

# py -2 slots-test.py
# Slots    => 0.615521153591
# Nonslots => 0.766582559582
