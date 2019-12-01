# 생성과 초기화를 커스터마이즈하기

class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaTwo.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaTwo):    # Eggs로부터 상속, MetaTwo의 인스턴스
    data = 1                            # 클래스 데이터 속성
    def meth(self, arg):                # 클래스 메서드 속성
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


# py -3 metaclass2.py 
# making class
# In MetaTwo.new: 
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7f386e55e9d8>}
# In MetaTwo.init:
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7f386e55e9d8>}
# ...init class object: ['__module__', 'data', 'meth', '__doc__']
# making instance
# data: 1 3
