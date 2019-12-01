# 다른 메타클래스 코딩 기법

# 단순한 팩토리 함수 사용하기

# 단순 함수도 메타클래스로 역할할 수 있음

def MetaFunc(classname, supers, classdict):
    print('In MetaFunc: ', classname, supers, classdict, sep='\n...')
    return type(classname, supers, classdict)

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaFunc):   # 마지막에 단순 함수를 실행
    data = 1                            # 함수는 클래스를 반환함
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))


# py -3 metaclass3.py 
# making class
# In MetaFunc: 
# ...Spam
# ...(<class '__main__.Eggs'>,)
# ...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7fe6e4c398c8>}
# making instance
# data: 1 3
