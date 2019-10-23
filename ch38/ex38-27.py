# __getattr__을 이용한 검증

# validate_getattr.py 파일

class CardHolder:
    acctlen = 8                         # 클래스 데이터
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                # 인스턴스 데이터
        self.name = name                # __setattr__이 호출됨
        self.age  = age                 # _acct는 맹글링되지 않고 name을 확인함
        self.addr = addr                # addr은 관리 속성이 아님
                                        # remain은 데이터가 없음

    def __getattr__(self, name):
        if name == 'acct':                             # 정의되지 않은 속성 가져오기
            return self._acct[:-3] + '***'             # name.age, addr는 정의되어 있음
        elif name == 'remain':
            return self.retireage - self.age           # __getattr__이 호출되지 않음
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'name':                             # 모든 속성에 대한 할당
            value = value.lower().replace(' ', '_')    # addr은 직접 저장됨
        elif name == 'age':                            # acct가 _acct로 변경됨
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name  = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invalid acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value                    # 무한 루프 방지


# py -3 validate_tester.py validate_getattr
# ...클래스 이름을 제외하면 프로퍼티와 결과가 같음...

# py -3 validate_tester2.py validate_getattr
# ...클래스 이름을 제외하면 프로퍼티와 결과가 같음...
