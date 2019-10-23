# validate_properties.py 파일

class CardHolder(object):               # 2.X에서는 "(object)"를 필요로 함
    acctlen = 8                         # Class data
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                    # 인스턴스 데이터
        self.name = name                    # 프로퍼티 setter 도구를 호출
        self.age  = age                     # __X는 클래스 이름을 포함하여 맹글링됨
        self.addr = addr                    # addr은 관리되지 않음
                                            # remain은 데이터가 없음

    def getName(self):
        return self.__name
    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value
    name = property(getName, setName)

    def getAge(self):
        return self.__age
    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value
    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'
    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invalid acct number')
        else:
            self.__acct = value
    acct = property(getAcct, setAcct)

    def remainGet(self):                    # 이미 속성으로 사용되고 있지 않다면
        return self.retireage - self.age    # 메서드가 아니라 속성일 수도 있음
    remain = property(remainGet)
