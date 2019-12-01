# 상속과 인스턴스

# metainstance.py 파일

class MetaOne(type):
    def __new__(meta, classname, supers, classdict):       # type 메서드 재정의
        print('In MetaOne.new:', classname)
        return type.__new__(meta, classname, supers, classdict)
    def toast(self):
        return 'toast'

class Super(metaclass=MetaOne):         # sub는 메타클래스를 상속받음
    def spam(self):                     # MetaOne은 두 클래스를 위해 두번 실행됨
        return 'spam'

class Sub(Super):                       # 슈퍼클래스: 상속 vs 인스턴스
    def eggs(self):                     # 클래스는 슈퍼클래스로부터 상속받음
        return 'eggs'                   # 하지만 메타클래스로부터 상속받지는 않음


from metainstance import *              # class문 실행: 메타클래스는 두번 실행
# In MetaOne.new: Super
# In MetaOne.new: Sub

X = Sub()                               # 사용자 정의 클래스의 일반 인스턴스
X.eggs()                                # Sub로부터 상속됨
# 'eggs'
X.spam()                                # Super로부터 상속됨
# 'spam'
X.toast()                               # 메타클래스로부터 상속되지 않음
# AttributeError: 'Sub' object has no attribute 'toast'


Sub.eggs(X)                             # 자신만의 메서드
# 'eggs'
Sub.spam(X)                             # Super로부터 상속
# 'spam'
Sub.toast()                             # metaclass로부터 획득
# 'toast'
Sub.toast(X)                            # 일반 클래스 메서드가 아님
# TypeError: toast() takes 1 positional argument but 2 were given


Sub.toast
# <bound method MetaOne.toast of <class 'metainstance.Sub'>>
Sub.spam
# <function Super.spam at 0x7f85a6d187b8>
X.spam
# <bound method Super.spam of <metainstance.Sub object at 0x7f85aa5e1eb8>>
