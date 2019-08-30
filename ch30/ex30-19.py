# 문자열 표현: __repr__과 __str__

class adder:
    def __init__(self, value=0):
        self.data = value       # 데이터 초기화
    def __add__(self, other):
        self.data += other      # other를 직접 더함(나쁜 형태?)

x = adder()                     # 기본 표현 방식
print(x)
# <__main__.adder object at 0x7f351075d080>
x
# <__main__.adder object at 0x7f351075d080>


class addrepr(adder):                       # __init__, __add__ 상속
    def __repr__(self):                     # 문자열 표현 추가
        return 'addrepr(%s)' % self.data    # 코딩된 문자열로 변환

x = addrepr(2)                              # __init__ 실행
x + 1                                       # __add__ 실행(x.add()가 더 나은가?)
x                                           # __repr__ 실행
addrepr(3)
print(x)                                    # __repr__ 실행
addrepr(3)
str(x), repr(x)                             # 둘 모두를 위해 __repr__ 실행
# ('addrepr(3)', 'addrepr(3)')
