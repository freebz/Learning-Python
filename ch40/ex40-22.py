# 메타클래스 기반의 보완

# 메타클래스로 확장 - 미래의 변경 사항을 더 잘 지원함

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham'] = hamfunc
        return type.__new__(meta, classname, supers, classdict)

class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value
    def spam(self):
        return self.value * 2

class Client2(metaclass=Extender):
    value = 'ni?'

X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))


# py -3 extend-meta.py 
# Ni!Ni!
# Ni!Ni!Ni!Ni!
# baconham
# ni?ni?ni?ni?
# baconham


# 메타클래스는 런타임 테스트를 기반으로 클래스를 설정할 수도 있음

class MetaExtend(type):
    def __new__(meta, classname, supers, classdict):
        if sometest():
            classdict['eggs'] = eggsfunc1
        else:
            classdict['eggs'] = eggsfunc2
        if someothertest():
            classdict['ham'] = hamfunc
        else:
            classdict['ham'] = lambda *args: 'Not suported'
        return type.__new__(meta, classname, supers, classdict)
