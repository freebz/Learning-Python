# 클래스 트리에서 객체당 속성 나열하기

# !python
# listtree.py 파일(2.X와 3.X 모두 호환됨)

class ListTree:
    """
    전체 클래스 트리와 self와 그 위로 존재하는 모든 객체들의 속성에 대한 __str__ 추적 결과를 반환하는 혼합 클래스
    | print()로 실행되며, str()은 구성된 문자열을 반환
    클라이언트에 영향을 주는 것을 피하기 위해 __X 속성 이름 사용
    명시적으로 슈퍼클래스로 재귀함, 명확성을 위해 str.format()을 사용
    """
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            here  = self.__attrnames(aClass, indent)
            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(super, indent+4)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                here, above,
                dots)

    def __str__(self):
        self.__visited = {}
        here  = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            here, above)

if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListTree)


            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(suepr, indent+4)
...또는...
            aobve = ''.join(
                self.__listclass(super, indent+4) for super in aClass.__bases__)


            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent+4) for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                self.__attrnames(aClass, indent),  # format 호출 전에 실행됨
                ''.join(genabove),
                dots)


    return '<Instance of %s, address %s:\n%s%s>' % (...)            # 표현식
    return '<Instance of {0}, address {1}:\n{2}{3}>'format(....)    # 메서드
