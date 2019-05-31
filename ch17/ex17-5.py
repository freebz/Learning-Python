# global문

X = 88                          # 전역 X

def func():
    global X
    X = 99                      # 전역 X: def 바깥 점위

func()
print(X)                        # 99를 출력


y, z = 1, 2                     # 모듈의 전역 변수
def all_global():
    global x                    # 할당될 전역 변수 선언
    x = y + z                   # LEGB 규칙에 의거, y와 z는 별도 선언이 필요 없음
