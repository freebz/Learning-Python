# 전역을 활용한 상태 정보: 하나의 사본만 가능

def tester(start):
    global state                # state을 모듈로 옮겨서 변경 가능하도록 함
    state = start               # global은 모듈 범위에서 변경이 가능하게 함
    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F('spam')                       # 각 호출은 공유된 전역 state를 1씩 증가시킴
# spam 0
F('eggs')
# eggs 1


G = tester(42)                  # 전역 범위의 state의 단일 사본을 재설정
G('toast')
# toast 42

G('bacon')
# bacon 43

F('ham')                        # 하지만 F의 카운터도 덮어써 버림!
# ham 44
