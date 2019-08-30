# 비교: __lt__, __gt__ 등

class C:
    data = 'spam'
    def __gt__(self, other):        # 3.X와 2.X 버전
        return self.data > other
    def __lt__(self, other):
        return self.data < other

X = C()
print(X > 'ham')                    # 참(__gt__ 실행)
print(X < 'ham')                    # 거짓(__lt__ 실행)
