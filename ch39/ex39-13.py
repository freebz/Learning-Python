# 유효 범위와 nonlocal 변수

def tracer(func):                       # 유효 범위와 nonlocal을 통한 상태 정보
    calls = 0                           # 클래스 속성 또는 전역 대신에 사용
    def wrapper(*args, **kwargs):       # calls는 전역이 아니라 함수별 값을 가짐
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):              # spam = tracer(spam)과 동일
    print(a + b + c)

@tracer
def eggs(x, y):                 # eggs = tracer(eggs)와 동일
    print(x ** y)

spam(1, 2, 3)                   # 실제로 wrapper 호출, func과 결합됨
spam(a=4, b=5, c=6)             # wrapper는 spam을 호출

eggs(2, 16)                     # 실제로 wrapper를 호출, eggs와 결합됨
eggs(4, y=4)                    # nonlocal calls는 데코레이션별 값을 가짐


# py -3 decorator4.py 
# call 1 to spam
# 6
# call 2 to spam
# 15
# call 1 to eggs
# 65536
# call 2 to eggs
# 256
