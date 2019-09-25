# 프록시 코딩 요건

class C(object):
    data = 'spam'
    def __getattr__(self, name):
        print('getattr: ' + name)
        return getattr(self.data, name)

X = C()
X.__getitem__(1)                # 전형적인 매핑은 가능하지만, 새로운 형식으로는 불가
# getattr: __getitem__
# 'p'

X[1]
# TypeError: 'C' object does not support indexing
type(X).__getitem__(X, 1)
# AttributeError: type object 'C' has no attribute '__getitem__'

X.__add__('eggs')               # +에 대해 상동: 인스턴스는 표현식에 대해서만 생략됨
# getattr: __add__
# 'spameggs'

X + 'eggs'
# TypeError: unsupported operand type(s) for +: 'C' and 'str'
type(X).__add__(X, 'eggs')
# AttributeError: type object 'C' has no attribute '__add__'


class C(object):                          # 새로운 형식: 3.X와 3.X
    data = 'spam'
    def __getattr__(self, name):          # 일반적인 이름을 잡아냄
        print('getattr: ' + name)
        return getattr(self.data, name)
    def __getitem__(self, i):             # 내장된 연산을 재정의함
        print('getitem: ' + str(i))
        return self.data[i]               # 표현식 또는 getattr를 실행
    def __add__(self, other):
        print('add: ' + other)
        return getattr(self.data, '__add__')(other)

X = C()
X.upper
# getattr: upper
# <built-in method upper of str object at 0x7f498559fdf8>
X.upper()
# getattr: upper
# 'SPAM'

X[1]                            # 내장된 연산(암묵적)
# getitem: 1
# 'p'
X.__getitem__(1)                # 이에 상응하는 전형적인 방식(명시적)
# getitem: 1
# 'p'
type(X).__getitem__(X, 1)       # 이에 상응하는 새로운 스타일의 방식
# getitem: 1
# 'p'

X + 'eggs'                      # +와 다른 연산에 대해서도 상동
# add: eggs
# 'spameggs'
X.__add__('eggs')
# add: eggs
# 'spameggs'
type(X).__add__(X, 'eggs')
# add: eggs
# 'spameggs'
