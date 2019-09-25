# 기본값에 미치는 영향

# py -2
dir(object)
# ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__',
# '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

class C: pass
C.__bases__                     # 고전 클래스는 object로부터 상속받지 않음
# ()
X = C()
X.__repr__
# AttributeError: C instance has no attribute '__repr__'

class C(object): pass           # 새 형식 클래스는 object 기본값을 상속받음
C.__bases__
# (<type 'object'>,)
X = C()
X.__repr__
# <method-wrapper '__repr__' of C object at 0x7f0476fb3390>

# py -3
class C: pass                   # 3.X에서 모든 클래스는 기본값을 갖게 된다는 것을 의미함
C.__bases__
# (<class 'object'>,)
C().__repr__
# <method-wrapper '__repr__' of C object at 0x7f4984c41588>
