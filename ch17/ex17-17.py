# 변경을 위해 nonlocal 이용하기

def tester(start):
    state = start               # 각각의 호출은 자신만의 상태를 가짐
    def nested(label):
        nonlocal state          # 바깥쪽 범위의 상태를 기억
        print(label, state)
        state += 1              # nonlocal을 사용한 경우 변경 가능
    return nested

F = tester(0)
F('spam')                       # 각각의 호출마다 state가 1씩 증가
# spam 0
F('ham')
# ham 1
F('eggs')
# eggs 2


G = tester(42)                  # 42에서 시작하는 새로운 tester 생성
G('spam')
# spam 42
G('eggs')                       # 내 상태 정보는 43으로 갱신
# eggs 43

F('bacon')                      # 하지만 F는 마지막 상태인 3
# bacon 3                       # 각 호출은 다른 상태 정보를 가지고 있음
