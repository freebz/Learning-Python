# bothmethods_decorators.py 파일

class Methods(object):          # 2.X에서 프로퍼티 설정을 위해 object 필요
    def imeth(self, x):         # 일반 인스턴스 메서드: self를 전달
        print([self, x])

    @staticmethod
    def smeth(x):               # 정적 메서드: 인스턴스가 전달되지 않음
        print([x])

    @classmethod
    def cmeth(cls, x):          # 클래스 메서드: 인스턴스가 아닌 클래스를 받음
        print([cls, x])

    @property                   # 프로퍼티: 가져오는 시점에 연산
    def name(self):
        return 'Bob ' + self.__class__.__name__
