# 진행하면서 테스트하기

# 증가하는 셀프 테스트 코드 추가하기

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay

bob = Person('Bob Smith')                           # 클래스를 테스트
sue = Person('Sue Jones', job='dev', pay=100000)    # __init__ 이 자동으로 수행
print(bob.name, bob.pay)                            # 첨부된 속성을 가져옴
print(sue.name, sue.pay)                            # sue와 bob의 속성은 다름


# python person.py
Bob Smith 0
Sue Jones 100000
