def tracer(func):                       # 유효 범위와 함수 속성을 통한 상태 정보
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    wrapper.calls = 0                   # calls는 전역이 아니라 함수별 값을 가짐
    return wrapper

@tracer
def spam(a, b, c):              # spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):                 # eggs = tracer(eggs)와 동일
    print(x ** y)

spam(1, 2, 3)                   # 실제로 wrapper를 호출, spam에 할당
spam(a=4, b=5, c=6)             # wrapper는 spam을 호출

eggs(2, 16)                     # 실제로 wrapper를 호출, eggs에 할당
eggs(4, y=4)                    # wrapper.calls는 데코레이션별 값을 가짐
