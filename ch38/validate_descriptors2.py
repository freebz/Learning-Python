# validate_descriptors2.py 파일: 클라이언트 인스턴스 상태 활용

class CardHolder(object):               # 모든 "(object)"는 2.X에서만 필요
    acctlen = 8                         # 클래스 데이터
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                # 클라이언트 인스턴스 데이터
        self.name = name                # __set__ 호출
        self.age  = age                 # __X는 필요 없음. 디스크립터에 있음
        self.addr = addr                # addr은 관리 속성이 아님
                                        # remain은 데이터 없음

    class Name(object):
        def __get__(self, instance, owner):     # 클래스 이름: CardHolder 지역 변수
            return instance.__name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            instance.__name = value
    name = Name()                               # class.name vs 맹글링된 속성 

    class Age(object):
        def __get__(self, instance, owner):
            return instance.__age               # 디스크립터 데이터를 사용
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                instance.__age = value
    age = Age()                                 # class.age vs 맹글링된 속성

    class Acct(object):
        def __get__(self, instance, owner):
            return instance.__acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:        # 인스턴스 클래스 데이터 사용
                raise TypeError('invalid acct number')
            else:
                instance.__acct = value               
    acct = Acct()                                     # class.acct vs 맹글링된 속성 
    
    class Remain(object):
        def __get__(self, instance, owner):
            return instance.retireage - instance.age  # Age.__get__ 호출
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')      # 그렇지 않으면 여기서 set이 허용됨
    remain = Remain()
