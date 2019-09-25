# -*- coding: utf-8 -*-
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
