# 객체 인터페이스 추적하기

class Wrapper:
    def __init__(self, object):
        self.wrapped = object                     # 객체 저장
    def __getattr__(self, attrname):
        print('Trace:', attrname)                 # 호출을 추적
        return getattr(self.wrapped, attrname)    # 호출을 위임

x = Wrapper([1,2,3])                              # 리스트를 감쌈
x.append(4)                                       # 리스트 메서드에 위임
# Trace: append
x.wrapped                                         # 내 멤버를 출력
# [1, 2, 3, 4]

x = Wrapper({"a": 1, "b": 2})                     # 딕셔너리를 감쌈
list(x.keys())                                    # 딕셔너리 메서드에 위임
# Trace: keys                                     # 3.X에서는 list() 사용
# ['a', 'b']
