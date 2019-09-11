# -*- coding: utf-8 -*-
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
