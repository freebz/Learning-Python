# -*- coding: utf-8 -*-
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
