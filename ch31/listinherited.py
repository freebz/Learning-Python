# -*- coding: utf-8 -*-
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
