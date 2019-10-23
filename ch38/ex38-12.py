# 디스크립터 안에서 상태 정보 사용하기

class DescState:                        # 인스턴스 상태를 이용. 2.X에서는 (object)
    def __init__(self, value):
        self.value = value
    def __get__(self, instance, owner): # 속성을 가져올 때 실행됨
        print('DescState get')
        return self.value * 10
    def __set__(self, instance, value): # 속성을 할당할 때 실행
        print('DescState set')
        self.value = value

# 클라이언트 클래스
class CalcAttrs:
    X = DescState(2)            # 디스크립터 클래스 속성
    Y = 3                       # 클래스 속성
    def __init__(self):
        self.Z = 4              # 인스턴스 속성

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)      # X는 계산이 되면, Y와 Z는 계산되지 않음
obj.X = 5                       # X에 대한 할당을 가로챔
CalcAttrs.Y = 6                 # Y는 클래스 안에서 재할당됨
obj.Z = 7                       # Z는 인스턴스 안에서 할당됨
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()              # X는 Y처럼 공유 데이터를 사용함!
print(obj2.X, obj2.Y, obj2.Z)


# py -3 desc-state-desc.py
# DescState get
# 20 3 4
# DescState set
# DescState get
# 50 6 7
# DescState get
# 50 6 4



class InstState:                # 인스턴스 상태를 이용. (object)는 2.X에서만 필요
    def __get__(self, instance, owner):
        print('InstState get')  # 클라이언트 클래스에 의해 설정된다고 가정
        return instance._X * 10
    def __set__(self, instance, value):
        print('InstState set')
        instance._X = value

# 클라이언트 클래스
class CalcAttrs:
    X = InstState()             # 디스크립터 클래스 속성
    Y = 3                       # 클래스 속성
    def __init__(self):
        self._X = 2             # 인스턴스 속성
        self.Z  = 4             # 인스턴스 속성

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)      # X가 계산되지만 나머지는 계산되지 않음
obj.X = 5                       # X에 대한 할당이 캐치됨
CalcAttrs.Y = 6                 # 클래스 내에서 Y에 대해 재할당
obj.Z = 7                       # 인스턴스 내에서 Z에 대한 할당
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()              # 하지만 이제 Z처럼 X도 다르다!
print(obj2.X, obj2.Y, obj2.Z)


# py -3 desc-state-inst.py
# InstState get
# 20 3 4
# InstState set
# InstState get
# 50 6 7
# InstState get
# 20 6 4


class DescBoth:
    def __init__(self, data):
        self.data = data
    def __get__(self, instance, owner):
        return '%s, %s' % (self.data, instance.data)
    def __set__(self, instance, value):
        instance.data = value

class Client:
    def __init__(self, data):
        self.data = data
    managed = DescBoth('spam')

I = Client('eggs')
I.managed                       # 두 가지 데이터 소스를 모두 보여 줌
# 'spam, eggs'
I.managed = 'SPAM'              # 인스턴스 데이터를 변경함
I.managed
# 'spam, SPAM'


I.__dict__
# {'data': 'SPAM'}
[x for x in dir(I) if not x.startswith('__')]
# ['data', 'managed']

getattr(I, 'data')
# 'SPAM'
getattr(I, 'managed')
# 'spam, SPAM'

for attr in (x for x in dir(I) if not x.startswith('__')):
    print('%s => %s' % (attr, getattr(I, attr)))

# data => SPAM
# managed => spam, SPAM
