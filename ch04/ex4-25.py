# 사용자 정의 클래스

class Worker:
    def __init__(self, name, pay):      # 생성 시에 초기화
        self.name = name                # self는 새로 생성된 객체
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]    # 공백으로 문자열 분할
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)     # 급여 정보 갱신


bob = Worker('Bob Smith', 50000)        # 두 개의 인스턴스 생성
sue = Worker('Sue Jones', 60000)        # 각각은 이름과 급여 속성을 가지고 있음
bob.lastName()                          # 메서드 호출: self는 bob
# 'Smith'
sue.lastName()                          # 여기서 slef는 sue
# 'Jones'
sue.giveRaise(.10)                      # sue의 급여 갱신
sue.pay
# 66000.0
