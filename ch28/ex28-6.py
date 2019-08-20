# 단계 2: 행위 메서드 추가하기

name = 'Bob Smith'              # 클래스 외부의 단순 문자열
name.split()                    # 성 추출
# ['Bob', 'Smith']
name.split()[-1]                # 여기서는 name이 성과 이름으로 구성되어 있다고 가정
# 'Smith'


pay = 100000                    # 클래스 외부의 단순 변수
pay *= 1.10                     # 10% 인상
print('%.2f' % pay)             # 또는 타이핑하기 좋아한다면 pay = pay * 1.10
# 110000.00                     # 또는 진짜 타이핑을 좋아한다면 pay = pay + (pay * .10)


# 내장된 빌트인 타입 처리: 문자열, 가변성

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1])                # 객체의 성을 추출
    sue.pay *= 1.10                            # 이 객체의 급여 인상
    print('%.2f' % sue.pay)


# Bob Smith 0
# Sue Jones 100000
# Smith
# 110000.00
