# 타입 검사에 미치는 영향

# py -3
class C: pass
class D: pass

c, d = C(), D()
type(c) == type(d)              # 3.X: 인스턴스의 클래스를 비교
# False

type(c), type(d)
# (<class '__main__.C'>, <class '__main__.D'>)
c.__class__, d.__class__
# (<class '__main__.C'>, <class '__main__.D'>)

c1, c2 = C(), C()
type(c1) == type(c2)
# True


# py -2
class C: pass
class D: pass

c, d = C(), D()
type(c) == type(d)              # 2.X: 모든 인스턴스는 동일 타입!
# True
c.__class__ == d.__class__      # 필요하면, 명시적으로 클래스를 비교할 것
# False

type(c), type(d)
# (<type 'instance'>, <type 'instance'>)
c.__class__, d.__class__
# (<class __main__.C at 0x7f0476f9c600>, <class __main__.D at 0x7f0476f9c598>)


# py -2
class C(object): pass
class D(object): pass

c, d = C(), D()
type(c) == type(d)              # 2.X의 새 형식 클래스: 3.X에서의 모든 클래스와 동일
# False

type(c), type(d)
# (<class '__main__.C'>, <class '__main__.D'>)
c.__class__, d.__class__
# (<class '__main__.C'>, <class '__main__.D'>)
