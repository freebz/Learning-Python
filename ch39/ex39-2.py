# 구현

def decorator(F):
    # 함수 F 처리
    return F

@decorator
def func(): ...                 # func = decorator(func)


def decorator(F):
    # 함수 F를 저장 또는 사용
    # 다른 호출 가능한 객체를 반환: 중첩된 함수나 __call__을 가진 클래스 등

@decorator
def func(): ...                 # func = decorator(func)


def decorator(F):               # @ 데코레이션 시점에
    def wrapper(*args):         # 래핑된 함수 호출 시
        # F와 args 사용
        # F(*args)는 원래 함수를 호출
    return wrapper

@decorator                      # func = decorator(func)
def func(x, y):                 # func은 데코레이터의 F에 전달됨
    ...

func(6, 7)                      # 6, 7은 wrapper의 *args에 전달됨


class decorator:
    def __init__(self, func):   # @ 데코레이션 시점에
        self.func = func
    def __call__(self, *args):  # 감싸인 함수 호출 시
        # self.func와 args 사용
        # self.func(*args)는 원래 함수를 호출

@decorator
def func(x, y):                 # func = decorator(func)
    ...                         # func은 __init__에 전달됨

func(6, 7)                      # 6, 7은 __call__의 *args에 전달됨
