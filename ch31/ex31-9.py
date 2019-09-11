# 3.X에서 언바운드 메서드는 함수

# py -3
class Selfless:
    def __init__(self, data):
        self.data = data
    def selfless(arg1, arg2):             # 3.X에서는 단순 함수
        return arg1 + arg2
    def normal(self, arg1, arg2):         # 호출될 때 인스턴스를 기대함
        return self.data + arg1 + arg2

X = Selfless(2)
X.normal(3, 4)                  # 자동으로 self에 인스턴스가 전달됨: 2+(3+4)
# 9
Selfless.normal(X, 3, 4)        # 메서드는 self를 기대함: 직접 전달
# 9
Selfless.selfless(3, 4)         # 인스턴스가 없음: 3.X에서는 동작, 2.X는 실패!
# 7


X.selfless(3, 4)
# TypeError: selfless() takes 2 positional arguments but 3 were given

Selfless.normal(3, 4)
# TypeError: normal() missing 1 required positional argument: 'arg2'
