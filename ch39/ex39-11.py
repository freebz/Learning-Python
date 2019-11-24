# 데코레이터 상태 유지 방식

# 클래스 인스턴스 속성

class tracer:
    def __init__(self, func):                 # @ 데코레이션할 때
        self.calls = 0                        # 인스턴스 속성을 통해 상태 정보
        self.func = func                      # 이후의 호출을 위해 함수를 저장함
    def __call__(self, *args, **kwargs):      # 원래의 함수를 호출할 때
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

@tracer
def spam(a, b, c):              # spam = tracer(spam)과 동일
    print(a + b + c)            # tracer.__init__을 호출

@tracer
def eggs(x, y):                 # eggs = tracer(eggs)와 동일
    print(x ** y)               # eggs를 tracer 객체에 감쌈

spam(1, 2, 3)                   # 실제로 tracer 인스턴스 호출: tracer.__call__실행
spam(a=4, b=5, c=6)             # spam은 인스턴스의 속성

eggs(2, 16)                     # 실제로 tracer 인스턴스 호출, self.func은 eggs
eggs(4, y=4)                    # self.calls은 데코레이션 별로 집계됨


# python decorator2.py
# call 1 to spam
# 6
# call 2 to spam
# 15
# call 1 to eggs
# 65536
# call 2 to eggs
# 256
