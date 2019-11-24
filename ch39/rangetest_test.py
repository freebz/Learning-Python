"""
파일 rangetest_test.py(3.X + 2.X)
주석 처리된 줄은 셸 명령 라인에서 "python -O"을 사용하지 않으면 TypeError 발생
"""
from __future__ import print_function # 2.X
from rangetest import rangetest

# 함수 테스트: 위치와 키워드 인수

@rangetest(arg=(0, 120))                # persinfo = rangetest(...)(persinfo)
def persinfo(name, age):
    print('%s is %s years old' % (name, age))

@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2013))
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))

persinfo('Bob', 40)
persinfo(age=40, name='Bob')
birthday(5, D=1, Y=1963)
#persinfo('Bob', 150)
#persinfo(age=150, name='Bob')
#birthday(5, D=40, Y=1963)

# 메서드 테스트: 위치와 키워드 인수

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay
                                        # giveRaise = rangetest(...)(giveRaise)
    @rangetest(percent=(0.0, 1.0))      # 이름 또는 위치로 전달되는 퍼센트
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

bob = Person('Bob Smith', 'dev', 100000)
sue = Person('Sue Jones', 'dev', 100000)
bob.giveRaise(.10)
sue.giveRaise(percent=.20)
print(bob.pay, sue.pay)
#bob.giveRaise(1.10)
#bob.giveRaise(percent=1.20)

# 생략된 기본 인수 테스트: 생략
@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)

omitargs(1, 2, 3, 4)
omitargs(1, 2, 3)
omitargs(1, 2, 3, d=4)
omitargs(1, d=4)
omitargs(d=4, a=1)
omitargs(1, b=2, d=4)
omitargs(d=8, c=7, a=1)

#omitargs(1, 2, 3, 11)                  # 잘못된 d
#omitargs(1, 2, 11)                     # 잘못된 c
#omitargs(1, 2, 3, d=11)                # 잘못된 d
#omitargs(11, d=4)                      # 잘못된 a
#omitargs(d=4, a=11)                    # 잘못된 a
#omitargs(1, b=11, d=4)                 # 잘못된 b
#omitargs(d=8, c=7, a=11)               # 잘못된 a
