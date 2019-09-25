# 사용자 정의 함수 데코레이터의 소개

class tracer:
    def __init__(self, func):   # 원래 버전을 기억하고 카운터를 초기화
        self.calls = 0
        self.func = func
    def __call__(self, *args):  # 나중 호출 시: 로직을 추가하고 원래 버전 실행
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)

@tracer                         # spam = tracer(spam)가 동일
def spam(a, b, c):              # spam을 데코레이터 객체 내부에 래핑
    return a + b + c

print(spam(1, 2, 3))            # 실제로 래핑 객체인 tracer 호출
print(spam('a', 'b', 'c'))      # 클래스 내 __call__ 호출


# python tracer1.py 
# call 1 to spam
# 6
# call 2 to spam
# abc


def tracer(func):               # 원래 함수를 기억
    def oncall(*args):          # 나중에 호출될 함수에 전달됨
        oncall.calls += 1
        print('call %s to %s' % (oncall.calls, func.__name__))
        return func(*args)
    oncall.calls = 0
    return oncall

class C:
    @tracer
    def spam(self, a, b, c): return a + b + c

x = C()
print(x.spam(1, 2, 3))
print(x.spam('a', 'b', 'c'))    # tracer1과 같은 결과가 출력됨(trace2.py 파일)
