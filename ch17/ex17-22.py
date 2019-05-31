# 함수 속성을 이용한 상태 정보: 3.X, 2.X 모두 사용 가능

def tester(start):
    def nested(label):
        print(label, nested.state) # nested는 바깥쪽 범위에 있음
        nested.state += 1          # nested가 아닌 속성을 변경
    nested.state = start           # 함수가 정의된 후, state를 초기화
    return nested

F = tester(0)
F('spam')                       # F는 stated가 첨부된 nested 함수
# spam 0
F('ham')
# ham 1
F.state                         # 또한 함수 외부에서 state에 접근 가능
# 2


G = tester(42)                  # G는 자신만의 state를 가지며, F를 덮어쓰지 않음
G('eggs')
# eggs 42
F('ham')
# ham 2

F.state                         # state는 호출별로 접근 가능함
# 3
G.state
# 43
F is G                          # 서로 다른 객체
# False
