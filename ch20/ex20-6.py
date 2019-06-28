# 제너레이터 함수와 제너레이터 표현식

# 제너레이터 함수의 실제 동작

def gensquares(N):
    for i in range(N):
        yield i ** 2            # 나중에 여기서 실행이 재개됨


for i in gensquares(5):         # 함수 실행을 재개하여
    print(i, end=' : ')         # 마지막에 산출도니 값을 출력

# 0 : 1 : 4 : 9 : 16 :


x = gensquares(4)
x
# <generator object gensquares at 0x7f60689b9b48>


next(x)                         # 3.X에서 x.__next__()와 같음
# 0
next(x)                         # 2.X에서는 x.next() 또는 next()를 사용하자
# 1
next(x)
# 4
next(x)
# 9
next(x)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration


y = gensquares(5)               # 그 자체가 반복자인 제너레이터를 반환
iter(y) is y                    # iter() 호출이 불필요함: 아무런 동작을 하지 않음
# True

next(y)                         # next()를 직접 호출할 수 있음
# 0
