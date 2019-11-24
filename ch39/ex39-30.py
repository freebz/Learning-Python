# 예제: '개별(Private)' 그리고 '공통(Public)' 속성들

# 개별 속성 구현하기

"""
파일 access1.py(3.X + 2.X)

클래스 인스턴스로부터 가져오는 속성을 위한 프라이버시 사용 예시로
파일 마지막의 셀프 테스트 코드를 참조할 것

다음과 동일한 데코레이터: Doubler = Private('data', 'size')(Doubler)
Private은 onDecorator를 반환하고, onDecorator는 onInstance를 반환하며,
각 onInstance의 인스턴스는 Doubler 인스턴스를 내장함
"""

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):                              # privates은 유효 범위에
    def onDecorator(aClass):                         # aClass는 유효 범위에
        class onInstance:                            # 인스턴스 속성에 감싸임
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)

            def __getattr__(self, attr):             # 내 attrs는 getattr를 호출하지 않음
                trace('get:', attr)                  # 나머지는 감싸인 객체에 있다고 가정
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):            # 외부에서의 접근
                trace('set:', attr, value)                 # 나머지는 일반적으로 실행
                if attr == 'wrapped':                      # 내 attrs을 허용
                    self.__dict__[attr] = value            # 루프 반복을 피함
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)     # 감싸인 객체 속성
        return onInstance                                  # 또는 __dict__ 사용
    return onDecorator

if __name__ == '__main__':
    traceMe = True

    @Private('data', 'size')                  # Doubler = Private(...)(Doubler)
    class Doubler:
        def __init__(self, label, start):
            self.label = label                # 대상 클래스 내부에서의 접근
            self.data = start                 # 가로채지 않음: 일반적으로 실행
        def size(self):
            return len(self.data)             # 메서드는 검사 없이 실행
        def double(self):                     # 프라이버시는 상속되지 않기 때문임
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s' % (self.label, self.data))

X = Doubler('X is', [1, 2, 3])
Y = Doubler('Y is', [-10, -20, -30])

# 다음은 모두 성공
print(X.label)                                # 대상 클래스 외부에서의 접근
X.display(); X.double; X.display()            # 가로챔: 검증하고 위임됨
print(Y.label)
Y.display(); Y.double()
Y.label = 'Spam'
Y.display()

# 다음은 모두 적절히 실패함
"""
print(X.size())                 # 'TypeError': private attribute fetch: size'를 출력함
print(X.data)
X.data = [1, 1, 1]
X.size = lambda S: 0
print(Y.data)
print(Y.size())
"""


# py -3 access1.py
# [set: wrapped <__main__.Doubler object at 0x7fc16ffb61d0>]
# [set: wrapped <__main__.Doubler object at 0x7fc16ffb6208>]
# [get: label]
# X is
# [get: display]
# X is => [1, 2, 3]
# [get: double]
# [get: display]
# X is => [1, 2, 3]
# [get: label]
# Y is
# [get: display]
# Y is => [-10, -20, -30]
# [get: double]
# [set: label Spam]
# [get: display]
# Spam => [-20, -40, -60]
