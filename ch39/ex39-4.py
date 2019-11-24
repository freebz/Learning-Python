# 클래스 데코레이터

# 사용법

@decorator                      # 클래스 데코레이션
class C:
    ...

x = C(99)                       # 인스턴스 생성


class C:
    ...
C = decorator(C)                # 클래스 이름과 데코레이터 결과를 재결합

x = C(99)                       # 근본적으로 decorator(C)(99)
