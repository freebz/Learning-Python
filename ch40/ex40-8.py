# 메타클래스 코딩

# 기본 메타클래스

class Meta(type):
    def __new__(meta, classname, supers, classdict):
        # 상속받은 type.__call__에 의해 실행됨
        return type.__new__(meta, classname, supers, classdict)


class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaOne):    # Eggs로부터 상속, MetaOne의 인스턴스
    data = 1                            # 클래스 데이터 속성
    def meth(self, arg):                # 클래스 메서드 속성
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


# py -3 metaclass1.py 
# making class
# In MetaOne.new:
# ...<class '__main__.MetaOne'>
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7f52f166f950>}
# making instance
# data: 1 3


from __future__ import print_function   # 2.X(에서만) 똑같이 실행하기 위해
class Eggs(object):                     # "object" 중 하나는 선택적임
class Spam(Eggs, object):
    __metaclass__ = MetaOne
