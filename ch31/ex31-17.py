# dir로 상속받은 속성 나열하기

# !python
# listinherited.py 파일(2.X와 3.X 모두 호환됨)

class ListInherited:
    """
    dir()을 사용하여 인스턴스 속성과 그 인스턴스의 클래스로부터 상속받은 이름을 수집.
    파이썬 3.X는 2.X보다 더 많은 이름을 보여 주는데 , 새 형식ㅂ 클래스 모델에서
    암묵적인 슈퍼크래스인 object 때문임. self._dict__가 아니라 getattr()에서 상속된 이름을 가져옴.
    __repr__이 아니라 __str__을 사응할 것. 그렇지 않으면 바운드 메서드를 출력할 때 루프가 발생하게 됨!
    """
    def __attrnames(self):
        result = ''
        for attr in dir(self):                             # 인스턴스 dir()
            if attr[:2] == '__' and attr[-2:] == '__':     # 내부 이름은 생략
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self, attr))
        return result

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                           self.__class__.__name__,        # 내 클래스 이름
                           id(self),                       # 내 주소
                           self.__attrnames())             # 이름 = 값 형태의 목록

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)


# py -2
# <Instance of Sub, address 140118579407976:
# 	_ListInherited__attrnames=<bound method Sub.__attrnames of <testmixin.Sub instance at 0x7f6fe626ec68>>
# 	__doc__
# 	__init__
# 	__module__
# 	__str__
# 	data1=spam
# 	data2=eggs
# 	data3=42
# 	ham=<bound method Sub.ham of <testmixin.Sub instance at 0x7f6fe626ec68>>
# 	spam=<bound method Sub.spam of <testmixin.Sub instance at 0x7f6fe626ec68>>
# >


# py -3
# <Instance of Sub, address 140420971825864:
# 	_ListInherited__attrnames=<bound method ListInherited.__attrnames of <testmixin.tester.<locals>.Sub object at 0x7fb64e250ac8>>
# 	__class__
# 	__delattr__
# 	__dict__
# 	__dir__
# 	__doc__
# 	__eq__
# 	__format__
# 	__ge__
# 	__getattribute__
# 	__gt__
# 	__hash__
# 	__init__
# 	__init_subclass__
# 	__le__
# 	__lt__
# 	__module__
# 	__ne__
# 	__new__
# 	__reduce__
# 	__reduce_ex__
# 	__repr__
# 	__setattr__
# 	__sizeof__
# 	__str__
# 	__subclasshook__
# 	__weakref__
# 	data1=spam
# 	data2=eggs
# 	data3=42
# 	ham=<bound method tester.<locals>.Super.ham of <testmixin.tester.<locals>.Sub object at 0x7fb64e250ac8>>
# 	spam=<bound method tester.<locals>.Sub.spam of <testmixin.tester.<locals>.Sub object at 0x7fb64e250ac8>>
# >


def __attrnames(self, indent=' '*4):
    result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-'*77, indent, '-'*77)
    unders = []
    for attr in dir(self):                                 # 인스턴스 dir()
        if attr[:2] == '__' and attr[-2:] == '__':         # 내부 이름은 생략
            unders.append(attr)
        else:
            display = str(getattr(self, attr))[:82-(len(indent) + len(attr))]
            result += '%s%s=%s\n' % (indent, attr, display)
    return result % ', '.join(unders)


# py -2
# <Instance of Sub, address 140222439278928:
# Unders-----------------------------------------------------------------------------
#     __doc__, __init__, __module__, __str__
# Others-----------------------------------------------------------------------------
#     _ListInherited__attrnames=<bound method Sub.__attrnames of <testmixin.Sub insta
#     data1=spam
#     data2=eggs
#     data3=42
#     ham=<bound method Sub.ham of <testmixin.Sub instance at 0x7f8814aec950>>
#     spam=<bound method Sub.spam of <testmixin.Sub instance at 0x7f8814aec950>>
# >


# py -3
# <Instance of Sub, address 140313830620296:
# Unders-----------------------------------------------------------------------------
#     __class__, __delattr__, __dict__, __dir__, __doc__, __eq__, __format__, __ge__, __getattribute__, __gt__, __hash__, __init__, __init_subclass__, __le__, __lt__, __module__, __ne__, __new__, __reduce__, __reduce_ex__, __repr__, __setattr__, __sizeof__, __str__, __subclasshook__, __weakref__
# Others-----------------------------------------------------------------------------
#     _ListInherited__attrnames=<bound method ListInherited.__attrnames of <testmixin
#     data1=spam
#     data2=eggs
#     data3=42
#     ham=<bound method tester.<locals>.Super.ham of <testmixin.tester.<locals>.Sub o
#     spam=<bound method tester.<locals>.Sub.spam of <testmixin.tester.<locals>.Sub o
# >
