# 내장된 기능이 특별한 경우

class C:                            # 상속 특별 케이스 #2...
    attr = 1                        # 내장된 기능은 단계를 건너뜀
    def __str__(self): return('class')

I = C()
I.__str__(), str(I)                 # 둘 모두 인스턴스에 없다면 클래스로부터
# ('class', 'class')

I.__str__ = lambda: 'instance'
I.__str__(), str(I)                 # 명시적 => 인스턴스, 내장된 기능 => 클래스!
# ('instance', 'class')

I.attr                              # 일반 또는 명시적인 이름들과 비대칭
# 1
I.attr = 2; I.attr
# 2


class D(type):
    def __str__(self): return('D class')

class C(D):
    pass
C.__str__(C), str(C)                # 명시적 => 슈퍼클래스, 내장된 기능 => 메타클래스!
# ('D class', "<class '__main__.C'>")

class C(D):
    def __str__(self): return('C class')
C.__str__(C), str(C)                # 명시적 => 클래스, 내장된 기능 => 메타클래스!
# ('C class', "<class '__main__.C'>")

class C(metaclass=D):
    def __str__(self): return('C class')
C.__str__(C), str(C)                # 내장된 기능 => 사용자 정의 메타클래스
# ('C class', 'D class')


class C(metaclass=D):
    pass
C.__str__(C), str(C)                # 명시적 => 객체, 내장된 기능 => 메타클래스
# ("<class '__main__.C'>", 'D class')

C.__str__
# <slot wrapper '__str__' of 'object' objects>

for k in (C, C.__class__, type): print([x.__name__ for x in k.__mro__])
# ['C', 'object']
# ['D', 'type', 'object']
# ['type', 'object']
