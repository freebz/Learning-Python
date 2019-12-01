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
