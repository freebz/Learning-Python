# __dict__로 인스턴스 속성 나열하기

#!python
# listinstance.py 파일(2.X와 3.X 모두 호환됨)

class ListInstance:
    """
    여기에서 작성된 __str__ 의 상속을 통해 인스턴스의 포맷이 갖춰진
    print() 또는 str()을 제공하는 혼합 클래스, self는 가장 낮은 클래스의 인스턴스임
    __X 이름은 클라이언트의 속성과의 충돌을 피함
    """
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                           self.__class__.__name__,    # 내 클래스의 이름
                           id(self),                   # 내 주소
                           self.__attrnames())         # 이름 = 값 목록

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInstance)


def __attrnames(self):
    return ''.join('\t%s=%s\n' % (attr, self.__dict__ [attr])
                   for attr in sorted(self.__dict__))


from listinstance import ListInstance
class Spam(ListInstance):           # __str__ 메서드 상속
    def __init__(self):
        self.data1 = 'food'
x = Spam()
print(x)                            # print()와 str()은 __str__을 실행
# <Instance of Spam, address 140526419167776:
# 	data1=food
# >


display = str(x)                    # 이스케이프를 해석하기 위해 이를 프린트
display
# '<Instance of Spam, address 140526419167776:\n\tdata1=food\n>'


x                                   # __repr__는 여전히 기본값 사용
# <__main__.Spam object at 0x7fcedb4bca20>


# testmixin0.py 파일
from listinstance import ListInstance    # lister 도구 클래스 가져오기

class Super:
    def __init__(self):                  # 슈퍼클래스의 __init__
        self.data1 = 'spam'              # 인스턴스 속성 생성
    def ham(self):
        pass

class Sub(Super, ListInstance):          # ham과 __str__을 혼합
    def __init__(self):                  # Lister는 self에 접근할 수 없음
        Super.__init__(self)
        self.data2 = 'eggs'              # 더 많은 인스턴스 속성들
        self.data3 = 42
    def spam(self):                      # 여기에서 다른 메서드 정의
        pass

if __name__ == '__main__':
    X = Sub()
    print(X)                             # 혼합 __str__을 실행


# python testmixin0.py
# <Instance of Sub, address 140389266451480:
# 	data1=spam
# 	data2=eggs
# 	data3=42
# >


# !python
# testmixin.py 파일 (2.X와 3.X 모두 호환됨)
"""
일반적인 리스터 혼합 테스터: 25장의 리로드 도구와 유사하지만, 테스터에 클래스 객체를 전달함(함수가 아니라),
그리고 testByNames는 31장의 팩토리 패턴에 따라 여기에서 이름 문자열로 모듈과 클래스를 로딩하는 것을 추가함
"""
import importlib

def tester(listerclass, sept=False):

    class Super:
        def __init__(self):     # 슈퍼클래스 __init__
            self.data1 = 'spam' # 인스턴스 속성 생성
        def ham(self):
            pass

    class Sub(Super, listerclass): # ham과 __str__ 혼합
        def __init__(self):        # Listers는 self 접근 가능
            Super.__init__(self)
            self.data2 = 'eggs'    # 더 많은 인스턴스 속성들
            self.data3= 42
        def spam(self):            # 여기에서 다른 메서드 정의
            pass

    instance = Sub()               # lister의 __str__로 인스턴스 전달
    print(instance)                # 혼합된 __str__ 실행(또는 str(x)를 통해)
    if sept: print('-' * 80)

def testByNames(modname, classname, sept=False):
    modobject   = importlib.import_module(modname) # 이름 문자열로 임포트
    listerclass = getattr(modobject, classname)    # 이름 문자열로 속성 가져옴
    tester(listerclass, sept)

if __name__ == '__main__':
    testByNames('listinstance', 'ListInstance', True)    # 세 방식 모두 테스트
    testByNames('listinherited', 'ListInherited', True)
    testByNames('listtree', 'ListTree', False)


# python listinstance.py
# <Instance of Sub, address 140301345707904:
# 	data1=spam
# 	data2=eggs
# 	data3=42
# >


# python testmixin.py
# <Instance of Sub, address 139654662528584:
# 	data1=spam
# 	data2=eggs
# 	data3=42
# >
# ... 그리고 두 개의 다른 리스터 클래스의 테스트를 기대하시라...


import listinstance
class C(listinstance.ListInstance): pass

x = C()
x.a, x.b, x.c = 1, 2, 3
print(x)
# <Instance of C, address 140526426100008:
# 	a=1
# 	b=2
# 	c=3
# >
