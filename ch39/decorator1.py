# decorator1.py 파일

class tracer:
    def __init__(self, func):           # @ 데코레이션할 때: 원래 함수를 저장
        self.calls = 0
        self.func = func
    def __call__(self, *args):          # 나중에 호출할 때: 원래 함수를 실행
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer
def spam(a, b, c):              # spam = tracer(spam)
    print(a + b + c)            # spam을 데코레이터 객체로 감쌈
