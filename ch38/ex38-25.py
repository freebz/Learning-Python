# 디스크립터를 이용한 검증

# 옵션 1: 공유된 디스크립터 인스턴스 상태를 통한 검증

# validate_descriptors1.py 파일: 공유 디스크립터 상태 사용

class CardHolder(object):               # (object) 상속은 2.X에서만 필요
    acctlen = 8                         # 클래스 데이터
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                # 인스턴스 데이터
        self.name = name                # __set__ 호출
        self.age  = age                 # __X는 필요 없음. 디스크립터에 있음
        self.addr = addr                # addr은 관리 속성이 아님
                                        # remain은 데이터 없음

    class Name(object):
        def __get__(self, instance, owner):           # 클래스 이름: CardHolder 지역 데이터
            return self.name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
    name = Name()

    class Age(object):
        def __get__(self, instance, owner):
            return self.age                           # 디스크립터 데이터 사용
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value
    age = Age()

    class Acct(object):
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:        # 인스턴스 클래스 데이터 사용
                raise TypeError('invalid acct number')
            else:
                self.acct = value
    acct = Acct()
    
    class Remain(object):
        def __get__(self, instance, owner):
            return instance.retireage - instance.age  # Age.__get__ 호출
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')      # remain 외에는 여기에서 set이 허용됨
    remain = Remain()


# python validate_tester.py validate_descriptors1
# ...클래스 이름을 제외하면 프로퍼티와 같은 결과가 출력됨...
