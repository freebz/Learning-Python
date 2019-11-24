# 구현

def decorator(C):
    # 클래스 C 처리
    return C

@decorator
class C: ...                    # C = decorator(C)


def decorator(C):
    # 클래스 C를 저장 또는 사용
    # 다른 호출 가능한 객체 반환: 중첩된 def.__call__을 가진 클래스 등

@decorator
class C: ...                    # C = decorator(C)


def decorator(cls):                             # @ 데코레이션 시
    class Wrapper:
        def __init__(self, *args):              # 인스턴스 생성 시
            self.wrapped = cls(*args)
        def __getattr__(self, name):            # 속성을 가져올 때
            return getattr(self.wrapped, name)
    return Wrapper

@decorator
class C:                        # C = decorator(C)
    def __init__(self, x, y):   # Wrapper.__init__에 의해 실행됨
        self.attr = 'spam'

x = C(6, 7)                     # 실제로 Wrapper(6, 7)을 호출
print(x.attr)                   # Wrapper.__getattr__ 실행, 'spam' 출력
