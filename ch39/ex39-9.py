# 데코레이터는 함수와 클래스도 관리

def decorator(O):
    # 함수 또는 클래스 O를 저장하거나 확장함
    return O

@decorator
def F(): ...                    # F = decorator(F)

@decorator
class C: ...                    # C = decorator(C)
