# 다른 호출 가능한 객체들

def square(arg):
    return arg ** 2             # 단순 함수(def 또는 lambda)

class Sum:
    def __init__(self, val):    # 호출 가능한 인스턴스
        self.val = val
    def __call__(self, arg):
        return self.val + arg

class Product:
    def __init__(self, val):    # 바운드 메서드
        self.val = val
    def method(self, arg):
        return self.val * arg

sobject = Sum(2)
pobject = Product(3)
actions = [square, sobject, pobject.method]    # 함수, 인스턴스, 메서드

for act in actions:                            # 셋 모두 동일한 방식으로 호출됨
    print(act(5))                              # 인수 하나짜리 호출 가능 객체를 호출

# 25
# 7
# 15
actions[-1](5)                                 # 인덱스, 컴프리헨션, maps
# 15

[act(5) for act in actions]
# [25, 7, 15]
list(map(lambda act: act(5), actions))
# [25, 7, 15]


class Negate:
    def __init__(self, val):    # 클래스도 호출 가능한 객체임
        self.val = -val         # 하지만 작업이 아닌 객체를 위해 호출됨
    def __repr__(self):         # 인스턴스 출력 포맷
        return str(self.val)

actions = [square, sobject, pobject.method, Negate]    # 클래스도 호출
for act in actions:
    print(act(5))

# 25
# 7
# 15
# -5
[act(5) for act in actions]     # __str__이 아니라 __repr__실행!
# [25, 7, 15, -5]

table = {act(5): act for act in actions}          # 3.X/2.7 딕셔너리 컴프리헨션
for (key, value) in table.items():
    print('{0:2} => {1}'.format(key, value))      # 3.6+/3.X str.format

# 25 => <function square at 0x7f800d461c80>
# 7 => <__main__.Sum object at 0x7f800d48df28>
# 15 => <bound method Product.method of <__main__.Product object at ...등등...>>
# -5 => <class '__main__.Negate'>
