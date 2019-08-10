# 최상위 레벨 코드에서는 문장 순서가 중요

func1()                         # 에러: "func1"은 아직 할당되지 않음

def func1():
    print(func2())              # OK: "func2"는 나중에 검색될 것임

func1()                         # 에러: "func2"는 아직 할당되지 않음

def func2():
    return "Hello"

func1()                         # OK: "func1"과 "func2"가 할당됨
