# 디스플레이 사용 노트

class Printer:
    def __init__(self, val):
        self.val = val
    def __str__(self):          # 인스턴스 자체를 위해 사용
        return str(self.val)    # 문자열 결과로 변환

objs = [Printer(2), Printer(3)]
for x in objs: print(x)         # 인스턴스가 프린트될 때 __str__ 실행
                                # 하지만 인스턴스가 리스트에 있을 때는 실행되지 않음
# 2
# 3
print(objs)
# [<__main__.Printer object at 0x7f351075de48>, <__main__.Printer object at 0x7f351075de80>]
objs
# [<__main__.Printer object at 0x7f351075de48>, <__main__.Printer object at 0x7f351075de80>]


class Printer:
    def __init__(self, val):
        self.val = val
    def __repr__(self):         # __str__이 없으면 print는 __repr__을 사용
        return str(self.val)    # 반복이나 중첩된 경우, __repr__이 사용됨
objs = [Printer(2), Printer(3)]
for x in objs: print(x)         # __str__이 없으므로: __repr__을 실행

# 2
# 3
print(objs)                     # __str__이 아니라 __repr__ 실행
# [2, 3]
objs
# [2, 3]
