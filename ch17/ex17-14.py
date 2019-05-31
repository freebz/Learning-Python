# 임의 범위 중첩

def f1():
    x = 99
    def f2():
        def f3():
            print(x)            # f1의 지역 범위에서 발견됨
        f3()
    f2()
f1()
# 99
