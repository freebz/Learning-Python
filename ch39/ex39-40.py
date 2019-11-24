# 구현 상세

# 함수 내부 검사

# 파이썬 3.X(그리고 호환성을 위해 2.6+)
def func(a, b, c, e=True, f=None):      # Args: 세 개는 필수, 두 개는 기본 인수
    x = 1                               # 두 개의 지역 변수
    y = 2

code = func.__code__                    # 함수 객체의 코드 객체
code.co_nlocals
# 7
code.co_varnames                        # 모든 지역 변수 이름들
# ('a', 'b', 'c', 'e', 'f', 'x', 'y')
code.co_varnames[:code.co_argcount]     # <== 처음 N 지역 변수가 기대되는 인수들
# ('a', 'b', 'c', 'e', 'f')


def catcher(*pargs, **kargs): print('%s, %s' % (pargs, kargs))

catcher(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5), {}
catcher(1, 2, c=3, d=4, e=5)        # 호출 시 인수들
# (1, 2), {'c': 3, 'd': 4, 'e': 5}


import sys                          # 하위 버전 호환성을 위해
tuple(sys.version_info)             # [0]은 주요 릴리즈 숫자
# (3, 6, 8, 'final', 0)
code = func.__code__ if sys.version_info[0] == 3 else func.func_code
