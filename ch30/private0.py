# -*- coding: utf-8 -*-
# 인스턴스 속성을 위한 프라이버시 모방하기: 파트 1

class PrivateExc(Exception): pass              # 예외는 파트 7에서 더 알아볼 예정임

class Privacy:
    def __setattr__(self, attrname, value):    # self.attrname = value에서
        if attrname in self.privates:
            raise PrivateExc(attrname, self)   # 사용자 정의 예외 생성 및 발생
        else:
            self.__dict__[attrname] = value    # 딕셔너리 키를 이용하여 루프를 피함

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'          # 더 잘하려면, 39장 참조!

if __name__ == '__main__':
    x = Test1()
    y = Test2()

    x.name = 'Bob'              # 성공
   #y.name = 'Sue'              # 실패
    print(x.name)

    y.age = 30                  # 성공
   #x.age = 40                  # 실패
    print(y.age)
