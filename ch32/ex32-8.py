# 모든 클래스는 'object'로부터 파생

class C: pass                   # 새 형식 클래스
X = C()
type(X), type(C)                # 타입은 클래스 인스턴스가 유래된 원천임
# (<class '__main__.C'>, <class 'type'>)


isinstance(X, object)
# True
isinstance(C, object)           # 클래스는 항상 object로부터 상속받음
# True


type('spam'), type(str)
# (<class 'str'>, <class 'type'>)

isinstance('spam', object)      # 내장된 타입(클래스)에서도 동일
# True
isinstance(str, object)
# True


type(type)                      # 모든 클래스는 타입이며, 역으로 모든 타입은 클래스임
# <class 'type'>
type(object)
# <class 'type'>

isinstance(type, object)        # type을 포함한 모든 클래스는 object로부터 파생됨
# True
isinstance(object, type)        # 타입은 클래스를 만들며, 타입은 클래스임
# True
type is object
# False
