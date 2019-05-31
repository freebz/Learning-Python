# 중첩된 범위, 기본 인수, lambda 함수

def func():
    x = 4
    action = (lambda n: x ** n) # 바깥쪽 def의 x를 기억
    return action

x = func()
print(x(2))                     # 4 ** 2인 16을 출력


def func():
    x = 4
    action = (lambda n, x=x: x ** n)   # x를 직접 전달함
    return action
