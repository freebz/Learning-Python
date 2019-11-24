# argtest_testmeth.py 파일
from argtest import rangetest, typetest

class C:
    @rangetest(a=(1, 10))
    def meth1(self, a):
        return a * 1000

    @typetest(a=int)
    def meth2(self, a):
        return a * 1000
