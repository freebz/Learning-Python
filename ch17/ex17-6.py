# 프로그램 설계: 전역 변수 최소화하기

X = 99
def func1():
    global X
    X = 88

def func2():
    global X
    X = 77
