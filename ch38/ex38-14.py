# __getattr__과 __getattribute__

# 기본 지식

def __getattr__(self, name):           # 정의되지 않은 속성을 가져올 때 [obj.name]
def __getattribute__(self, name):      # 모든 속성을 가져올 때 [obj.name]
def __setattr__(self, name, value):    # 모든 속성 할당 시 [obj.name=value]
def __delattr__(self, name):           # 모든 속성 삭제 시 [del obj.name]


class Catcher:
    def __getattr__(self, name):
        print('Get: %s' % name)
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))

X = Catcher()
X.job                           # 'Get: job' 출력
X.pay                           # 'Get: pay' 출력
X.pay = 99                      # 'Set; pay 99' 출력


class Catcher(object):                   # 2.X에서 (object) 필요
    def __getattribute__(self, name):    # getattr과 동일하게 동작
        print('Get: %s' % name)          # 보통 루프가 발생할 수 있음
    ...이하는 똑같음...


class Wrapper:
    def __init__(self, object):
        self.wrapped = object                     # object 저장
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)               # 가져오기를 추적함
        return getattr(self.wrapped, attrname)    # 가져오기 위임

X = Wrapper([1, 2, 3])
X.append(4)                                       # "Trace: append:" 출력 
print(X.wrapped)                                  # "[1, 2, 3, 4]" 출력
