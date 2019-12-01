# 메타클래스 모델

# 클래스는 type의 인스턴스

# py -3                               # 3.X에서
type([]), type(type([]))              # 리스트 인스턴스는 리스트 클래스로부터 생성됨
# (<class 'list'>, <class 'type'>)    # 리스트 클래스는 타입 클래스로부터 생성됨
type(list), type(type)                # 타입 이름을 제외하고 동일함
# (<class 'type'>, <class 'type'>)    # type의 타입은 type: 계층 구조 꼭대기


# py -2
type([]), type(type([]))              # 2.X에서 type은 약간 다름
# (<type 'list'>, <type 'type'>)
type(list), type(type)
# (<type 'type'>, <type 'type'>)


# py -3
class C: pass                   # 3.X 클래스 객체(새로운 형식)
X = C()                         # 클래스 인스턴스 객체

type(X)                         # 인스턴스는 클래스의 인스턴스
# <class '__main__.C'>
X.__class__                     # 인스턴스의 클래스
# <class '__main__.C'>

type(C)                         # 클래스는 type의 인스턴스
# <class 'type'>
C.__class__                     # 클래스의 클래스는 type
# <class 'type'>


# py -2
class C(object): pass           # 2.X에서 새 형식 클래스.
X = C()                         # 클래스들은 클래스를 가짐

type(X)
# <class '__main__.C'>
X.__class__
# <class '__main__.C'>

type(C)
# <class 'type'>
C.__class__
# <class 'type'>


# py -2
class C: pass                   # 2.X에서의 고전 클래스
X = C()                         # 클래스는 클래스를 가지고 있지 않음

type(X)
# <type 'instance'>
X.__class__
# <class __main__.C at 0x7fd7015a7598>

type(C)
# <type 'classobj'>
C.__class__
# AttributeError: class C has no attribute '__class__'
