# 코드를 두 방식으로 사용하기

# 이 파일이 실행/테스트됨과 동시에 임포트될 수 있도록 구성

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay

if __name__ == '__main__':                       # 테스트를 위해 실행될 때만
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)


# person.py
Bob Smith 0
Sue Jones 100000

# python
import person
