# 바운드 메서드와 다른 호출 가능한 객체들

class Number:
    def __init__(self, base):
        self.base = base
    def double(self):
        return self.base * 2
    def triple(self):
        return self.base * 3

x = Number(2)                                     # 클래스 인스턴스 객체
y = Number(3)                                     # 상태 + 메서드
z = Number(4)
x.double()                                        # 일반적인 즉시 호출
# 4

acts = [x.double, y.double, y.triple, z.double]   # 바운드 메서드들의 리스트
for act in acts:                                  # 호출이 지연됨
    print(act())                                  # 함수인 것처럼 호출
# 4
# 6
# 9
# 8


bound = x.double
bound.__self__, bound.__func__
# (<__main__.Number object at 0x...등등...>, <function Number.double at 0x...등등...>)
bound.__self__.base
# 2
bound()                         # bound.__func__(bound.__self__, ...)를 호출
# 4
