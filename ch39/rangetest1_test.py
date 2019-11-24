# rangetest1_test.py 파일
from __future__ import print_function # 2.X
from rangetest1 import rangetest
print(__debug__)                        # 만약 "python -O main.py"이라면 False

@rangetest((1, 0, 120))                 # persinfo = rangetest(...)(persinfo)
def persinfo(name, age):                # age는 0..120 사이에 있어야...
    print('%s is %s years old' % (name, age))

@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2009])
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay

    @rangetest([1, 0.0, 1.0])           # giveRaise = rangetest(...)(giveRaise)
    def giveRaise(self, percent):       # 여기에서 Arg 0은 self 인스턴스임
        self.pay = int(self.pay * (1 + percent))

# 주석 처리된 줄은 셸 명령 라인에서 "python -O"를 사용하지 않으면 TypeError 발생

persinfo('Bob Smith', 45)               # 실제로 onCall(...)을 상태 정보와 함께 실행
#persinfo('Bob Smith', 200)             # 만약 -O 명령 라인 인수가 사용되면 person 실행

birthday(5, 31, 1963)
#birthday(5, 32, 1963)

sue = Person('Sue Jones', 'dev', 100000)
sue.giveRaise(.10)                      # 실제로 onCall(slef, .10)을 실행
print(sue.pay)                          # 또는 -O의 경우 giveRaise(self, .10) 실행
#sue.giveRaise(1.10)
#print(sue.pay)
