# 타입 모델 변경

# py -2
class C: pass                   # 2.X에서의  고전 클래스
I = C()                         # 클래스로부터 만들어진 인스턴스
type(I), I.__class__
# (<type 'instance'>, <class __main__.C at 0x7f0476f9c600>)

type(C)                         # 하지만 클래스는 타입과 다름
# <type 'classobj'>
C.__class__
# AttributeError: class C has no attribute '__class__'

type([1, 2, 3]), [1, 2, 3].__class__
# (<type 'list'>, <type 'list'>)

type(list), list.__class__
# (<type 'type'>, <type 'type'>)


# py -2
class C(object): pass           # 2.X의 새 형식 클래스

I = C()                         # 인스턴스의 타입은 그 인스턴스가 유래된 클래스
type(I), I.__class__
# (<class '__main__.C'>, <class '__main__.C'>)

type(C), C.__class__            # 클래스는 사용자 정의 타입
# (<type 'type'>, <type 'type'>)


# py -3
class C: pass

I = C()                         # 3.X에서의 모든 클래스는 새로운 형식임
type(I), I.__class__            # 인스턴스의 타입은 인스턴스가 유래된 클래스임
# (<class '__main__.C'>, <class '__main__.C'>)

type(C), C.__class__            # 클래스는 타입이며, 타입은 클래스임
# (<class 'type'>, <class 'type'>)

type([1, 2, 3]), [1, 2, 3].__class__
# (<class 'list'>, <class 'list'>)

type(list), list.__class__      # 클래스와 내장된 타입은 같은 동작을 수행
# (<class 'type'>, <class 'type'>)
