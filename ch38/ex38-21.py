# 관리 기법 비교

# 두 개의 동적으로 연산되는 속성(프로퍼티 사용)

class Powers(object):           # (object)는 2.X에서만 필요
    def __init__(self, square, cube):
        self._square = square   # _square는 기본값
        self._cube   = cube     # square는 프로퍼티 이름

    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)

X = Powers(3, 4)
print(X.square)                 # 3 ** 2 = 9
print(X.cube)                   # 4 ** 3 = 64
X.square = 5
print(X.square)                 # 5 ** 2 = 25


# 동일한 코드와 디스크립터 사용(인스턴스 단위 상태)

class DescSquare(object):
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value

class DescCube(object):
    def __get__(self, instance, owner):
        return instance._cube ** 3

class Powers(object):           # (object)는 2.X에서만 필요
    square = DescSquare()
    cube   = DescCube()
    def __init__(self, square, cube):
        self._square = square   # "self.square = square"도 정상적으로 동작하는데,
        self._cube   = cube     # 이는 dest.__set__을 촉발하기 때문임

X = Powers(3, 4)
print(X.square)                 # 3 ** 2 = 9
print(X.cube)                   # 4 ** 3 = 64
X.square = 5
print(X.square)                 # 5 ** 2 = 25


# 동일한 코드와 범용적인 __getattr__을 이용한 정의되지 않은 속성 가로채기

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube   = cube

    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr:' + name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value    # 또는 객체 사용
        else:
            self.__dict__[name] = value

X = Powers(3, 4)
print(X.square)                 # 3 ** 2 = 9
print(X.cube)                   # 4 ** 3 = 64
X.square = 5
print(X.square)                 # 5 ** 2 = 25


# 동일하지만 범용적인 __getattribute__를 이용해 모든 속성을 가로챔

class Powers(object):           # (object)는 2.X에서만 필요
    def __init__(self, square, cube):
        self._square = square
        self._cube   = cube

    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'square':
            object.__setattr__(self, '_square', value)    # 또는 __dict__ 사용
        else:
            object.__setattr__(self, name, value)

X = Powers(3, 4)
print(X.square)                 # 3 ** 2 = 9
print(X.cube)                   # 4 ** 3 = 64
X.square = 5
print(X.square)                 # 5 ** 2 = 25


# 9
# 64
# 25
