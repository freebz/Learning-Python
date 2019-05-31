# 왜 nonlocal인가? 상태 유지 방법들

# nonlocal을 활용한 상태 정보: 3.X에서만 가능

def tester(start):
    state = start               # 각각의 호출은 자신만의 상태를 가짐
    def nested(label):
        nonlocal state          # 바깥쪽 범위의 상태를 기억함
        print(label, state)
        state += 1              # 비지역인 경우 변경 가능
    return nested

F = tester(0)
F('sapm')                       # 상태는 클로저 안에서만 보임
# sapm 0
F.state
# AttributeError: 'function' object has no attribute 'state'
