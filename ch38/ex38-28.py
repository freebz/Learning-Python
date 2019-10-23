# __getattribute__를 이용한 검증

# validate_getattribute.py 파일

class CardHolder(object):               # "(object)"는 2.X에서만 필요
    acctlen = 8                         # 클래스 데이터
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                       # 인스턴스 데이터
        self.name = name                       # 이렇게 하면 __setattr__이 실행됨
        self.age  = age                        # acct는 맹글링되지 않음, name으로 확인함
        self.addr = addr                       # addr은 관리되지 않음
                                               # 남아 있는 데이터는 없음

    def __getattribute__(self, name):
        superget = object.__getattribute__           # 루프를 돌지 않고 한 단계 올라감
        if name == 'acct':                           # 모든 속성 할당
            return superget(self, 'acct')[:-3] + '***'
        elif name == 'remain':
            return superget(self, 'retireage') - superget(self, 'age')
        else:
            return superget(self, name)              # naem, get, addr: 저장됨

    def __setattr__(self, name, value):
        if name == 'name':                            # 모든 속성 할당
            value = value.lower().replace(' ', '_')  # 주소를 직접 저장
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value                  # 루프 방지. 원래 이름 사용
