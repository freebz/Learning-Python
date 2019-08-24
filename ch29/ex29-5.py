# 슈퍼클래스 생성자 호출하기

class Super:
    def __init__(self, x):
        ...기본 코드...

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)         # 슈퍼클래스의 __init__ 실행
        ...(서브클래스의) 자체 코드...    # 자체 __init__ 액션 실행

I = Sub(1, 2)
