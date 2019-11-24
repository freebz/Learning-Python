# 데코레이터 인수

@decorator(A, B)
def F(arg):
    ...

F(99)


def F(arg):
    ...
F = decorator(A, B)(F)          # F를 데코레이터의 반환값의 결과에 재결합시킴

F(99)                           # 근본적으로 decorator(A, B)(F)(99)를 호출


def decorator(A, B):
    # A, B를 저장하거나 사용함
    def actualDecorator(F):
        # 함수 F를 저장하거나 사용함
        # 호출 가능한 객체 반환: 중첩된 def, __call__를 갖는 클래스 등
        return callable
    return actualDecorator
