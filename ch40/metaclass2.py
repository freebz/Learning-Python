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
