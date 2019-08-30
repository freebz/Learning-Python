# 파이썬 2.X의 __cmp__ 메서드

class C:
    data = 'spam'                       # 2.X에서만
    def __cmp__(self, other):           # __cmp__는3x에서는 사용하지 않음
        return cmp(self.data, other)    # cmp는 3.X에서는 정의되지 않음

X = C()
print(X > 'ham')                        # 참(__cmp__ 실행)
print(X < 'ham')                        # 거짓(__cmp__ 실행)


class C:
    data = 'spam'
    def __cmp__(self, other):
        return (self.data > other) - (self.data < other)
