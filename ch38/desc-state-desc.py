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
