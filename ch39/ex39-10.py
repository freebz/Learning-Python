# 함수 데코레이터 코딩하기

# 호출 추적하기

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


from decorator1 import spam

spam(1, 2, 3)                   # 실제로 tracer 래퍼 객체를 호출함
# call 1 to spam
# 6

spam('a', 'b', 'c')             # 클래스의 __call__ 호출
# call 2 to spam
# abc

spam.calls                      # 래퍼 상태 정보에 있는 호출 횟수
# 2
spam
# <decorator1.tracer object at 0x7f858328edd8>


calls = 0
def tracer(func, *args):
    global calls
    calls += 1
    print('call %s to %s' % (calls, func.__name__))
    func(*args)

def spam(a, b, c):
    print(a, b, c)

spam(1, 2, 3)                   # 추적되지 않는 일반적인 호출: 우연?
# 1 2 3

tracer(spam, 1, 2, 3)           # 데코레이터 없이 추적되는 특별한 호출
# call 1 to spam
# 1 2 3
