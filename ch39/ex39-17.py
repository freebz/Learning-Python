# 디스크립터를 이용해 메서드 데코레이트하기

class Descriptor(object):
    def __get__(self, instance, owner): ...
class Subject:
    attr = Descriptor()

X = Subject()
X.attr           # 대략 Descriptor.__get__(Subject.attr, X, Subject)를 실행


class tracer(object):                         # 데코레이터 + 디스크립터
    def __init__(self, func):                 # @ 데코레이션할 때
        self.calls = 0                        # 다음 호출을 위해 func을 저장
        self.func  = func
    def __call__(self, *args, **kwargs):      # 원래 함수를 호출할 때
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):       # 메서드 속성을 가져올 때
        return wrapper(self, instance)

class wrapper:
    def __init__(self, desc, subj):           # 두 인스턴스 모두 저장
        self.desc = desc                      # 호출을 데코레이터와 디스크립터에 전달
        self.subj = subj
    def __call__(self, *args, **kwargs):
        return self.desc(self.subj, *args, **kwargs)    # tracer.__call__을 실행

@tracer
def spam(a, b, c):                                      # spam = tracer(spam)
    ...이전과 동일...

class Person:
    @tracer
    def giveRaise(self, percent):                       # giveRaise = tracer(giveRaise)
        ...이전과 동일...                               # giveRaise를 디스크립터로 만듬


sue.giveRaise(.10)              # __get__ 실행 후 __call__ 실행


class tracer(object):
    def __init__(self, func):                 # @ 데코레이션할 때
        self.calls = 0                        # 나중 호출을 위해 func을 저장
        self.func = func
    def __call__(self, *args, **kwargs):      # 원래 함수를 호출할 때
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):               # 메서드를 가져올 때
        def wrapper(*args, **kwargs):                 # 두 인스턴스 모두 저장
            return self(instance, *args, **kwargs)    # __call__ 실행
        return wrapper


class tracer(object):                         # 함수가 아니라 메서드를 위해서!
    def __init__(self, meth):                 # @ 데코레이션할 때
        self.calls = 0
        self.meth  = meth
    def __get__(self, instance, owner):       # 메서드 가져올 때
        def wrapper(*args, **kwargs):         # 메서드 호출 시: self+인스턴스를 갖는 프록시
            self.calls += 1
            print('call %s to %s' % (self.calls, self.meth.__name__))
            return self.meth(instance, *args, **kwargs)
        return wrapper

class Person:
    @tracer                                   # 클래스 메서드에 적용
    def giveRaise(self, percent):             # giveRaise = tracer(giveRaise)
        ...                                   # giveRaise를 디스크립터로 만들어줌

@tracer                                       # 하지만 단순 함수에서는 실패
def spam(a, b, c):                            # spam = tracer(spam)
    ...                                       # 여기에서는 속성을 가져오지 않음
