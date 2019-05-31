# 클래스를 활용한 상태 정보: 명시적인 속성(미리 보기)

class tester:                   # 클래스 기반 방식(파트 6 참고)
    def __init__(self, start):  # 객체 생성 시
        self.state = start      # 새 객체에 상태를 명시적으로 저장
    def nested(self, label):
        print(label, self.state) # 상태를 명시적으로 참조함
        self.state += 1          # 항상 변경 가능함

F = tester(0)                   # 인스턴스를 생성, __init__ 실행
F.nested('spam')                # F는 self에 전달됨
# spam 0
F.nested('ham')
# ham 1


G = tester(42)                  # 각 인스턴스는 상태에 대한 새 사본을 가짐
G.nested('toast')               # 하나를 변경해도 다른 것에 영향을 주지 않음
# toast 42
G.nested('bacon')
# bacon 43

F.nested('eggs')                # F의 상태는 그대로 유지됨
# eggs 2
F.state                         # 상태는 클래스 외부에서도 접근 가능함
# 3


class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):      # 직접 인스턴스 호출하는 것을 가로챔
        print(label, self.state)    # 따라서 nested()가 필요 없음
        self.state += 1

H = tester(99)
H('juice')                          # __call__을 호출함
# juice 99
H('pancakes')
# pancakes 100
