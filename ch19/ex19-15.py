# 범위: 람다 또한 중첩될 수 있다

def action(x):
    return (lambda y: x + y)    # x를 기억하는 함수를 만들고 반환

act = action(99)
act
# <function action.<locals>.<lambda> at 0x7f080d8c9e18>
act(2)                          # 반환된 동작을 호출
# 101


action = (lambda x: (lambda y: x + y))
act = action(99)
act(3)
# 102
((lambda x: (lambda y: x + y))(99))(4)
# 103
