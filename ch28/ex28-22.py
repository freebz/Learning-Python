# 우리 클래스의 최종 형태

# classtools.py 파일(새로 변경한 버전)
...앞서 작성한 내용과 동일...

# person.py 파일(최종 버전)
"""
people에 대한 정보를 기록하고 처리함
이 클래스들을 테스트하려면 이 파일을 직접 실행하면 됨
"""
from classtools import AttrDisplay # 일반적인 디스플레이 도구 사용

class Person(AttrDisplay):      # 이 레벨에서 repr을 혼합
    """
    person의 기록을 생성하고 처리
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):         # 마지막 항목이 성이라 가정
        return self.name.split()[-1]

    def giveRaise(self, percent): # Percent는 0..1 사이어야 함
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    """
    특별한 요건으로 커스터마이즈된 Person
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay) # 직업명은 함축됨

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)


# python person.py
# [Person: job=None, name=Bob Smith, pay=0]
# [Person: job=dev, name=Sue Jones, pay=100000]
# Smith Jones
# [Person: job=dev, name=Sue Jones, pay=110000]
# Jones
# [Manager: job=mgr, name=Tom Jones, pay=60000]
