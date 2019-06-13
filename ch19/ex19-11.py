# 익명 함수: 람다

# 람다의 기본

def func(x, y, z): return x + y + z

func(2, 3, 4)
# 9


f = lambda x, y, z: x + y + z
f(2, 3, 4)
# 9


x = (lambda a="fee", b="fie", c="foe": a + b + c)
x("wee")
# 'weefiefoe'


def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)  # 바깥쪽 def 범위의 title
    return action                         # 함수 객체 반환

act = knights()
msg = act('robin')                        # 'robin'이 x에 전달
msg
# 'Sir robin'

act                                       # act: 실행 결과가 아닌 함수
# <function knights.<locals>.<lambda> at 0x7f8838a7df28>
