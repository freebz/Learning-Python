# 객체 지향 프로그래밍과 위임: '래퍼' 프록시 객체

class Wrapper:
    def __init__(self, object):
        self.wrapped = object                     # object 저장
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)               # 호출 추적
        return getattr(self.wrapped, attrname)    # 호출 위임


from trace import Wrapper
x = Wrapper([1, 2, 3])          # 리스트를 래핑
x.append(4)                     # 리스트 메서드에 위임
# Trace: append
x.wrapped                       # 내장 객체들 출력
# [1, 2, 3, 4]

x = Wrapper({'a': 1, 'b': 2})   # 딕셔너리를 래핑
list(x.keys())                  # 딕셔너리 메서드에 위임
# Trace: keys
# ['a', 'b']
