# 네임스페이스 딕셔너리: 리뷰

class Super:
    def hello(self):
        self.data1 = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'


X = Sub()
X.__dict__                      # 인스턴스 네임스페이스 딕셔너리
# {}
X.__class__                     # 인스턴스의 클래스
# <class '__main__.Sub'>
Sub.__bases__                   # 클래스의 슈퍼클래스
# (<class '__main__.Super'>,)
Super.__bases__                 # () 파이썬 2.X의 빈 튜플
# (<class 'object'>,)


Y = Sub()
X.hello()
X.__dict__
# {'data1': 'spam'}

X.hola()
X.__dict__
# {'data1': 'spam', 'data2': 'eggs'}

list(Sub.__dict__.keys())
# ['__module__', 'hola', '__doc__']
list(Super.__dict__.keys())
# ['__module__', 'hello', '__dict__', '__weakref__', '__doc__']

Y.__dict__
# {}


X.data1, X.__dict__['data1']
# ('spam', 'spam')

X.data3 = 'toast'
X.__dict__
# {'data1': 'spam', 'data2': 'eggs', 'data3': 'toast'}

X.__dict__['data3'] = 'ham'
X.data3
# 'ham'
