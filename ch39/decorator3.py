calls = 0
def tracer(func):                    # 유효 범위와 전역을 통한 상태 정보
    def wrapper(*args, **kwargs):      # 클래스 속성 대신
        global calls                   # calls는 전역, 함수별 값은 아님
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

spam(1, 2, 3)                   # 실제로 wrapper 호출, spam에 할당
spam(a=4, b=5, c=6)             # wrapper는 spam을 호출

eggs(2, 16)                     # 실제로 wrapper 호출, eggs에 할당
eggs(4, y=4)                    # 전역 calls는 데코레이션별 값이 아님!
