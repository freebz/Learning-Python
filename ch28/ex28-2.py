# 생성자 코딩하기

# 레코드 필드 초기화 추가

class Person:
    def __init__(self, name, job, pay): # 생성자는 세개의 인수를 취함
        self.name = name                # 생성될 때 필드를 채움
        self.job  = job                 # self는 새로운 인스턴스 객체임
        self.pay  = pay


# 생성자 인수에 대한 기본값 추가

class Person:
    def __init__(self, name, job=None, pay=0): # 일반 함수 인수
        self.name = name
        self.job  = job
        self.pay  = pay
