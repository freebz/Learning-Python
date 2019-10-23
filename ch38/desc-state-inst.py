
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
