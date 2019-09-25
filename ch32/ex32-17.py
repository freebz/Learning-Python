# 일반적으로 슬롯과 그 밖의 다른 '가상' 속성을 다루기

class Slotful:
    __slots__ = ['a', 'b', '__dict__']
    def __init__(self, data):
        self.c = data

I = Slotful(3)
I.a, I.b = 1, 2
I.a, I.b, I.c                       # 일반적으로 속성 가져오기
# (1, 2, 3)

I.__dict__                          # __dict__와 슬롯 모두 스토로지
# {'c': 3}
[x for x in dir(I) if not x.startswith('__')]
# ['a', 'b', 'c']

I.__dict__['c']                     # __dict__가 유일한 속성의 원천
# 3
getattr(I, 'c'), getattr(I, 'a')    # dir+getattr은 __dict__보다 범위가 넓음
# (3, 1)                            # 슬롯, 프로퍼티, 디스크립터에 적용

for a in (x for x in dir(I) if not x.startswith('__')):
    print(a, getattr(I, a))

# a 1
# b 2
# c 3
