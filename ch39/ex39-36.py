# 다른 방식으로 구현하기: __getattribute__ 삽입, 호출 스택 검사

# 메서드 삽입: access2.py code의 나머지 부분은 이전과 동일

def accessControl(failIf):
    def onDecorator(aClass):
        def getattributes(self, attr):
            trace('get:', attr)
            if failIf(attr):
                raise TypeError('private attribute fetch: ' + attr)
            else:
                return object.__getattribute__(self, attr)

        def setattributes(self, attr, value):
            trace('set:', attr)
            if failIf(attr):
                raise TypeError('private attribute change: ' + attr)
            else:
                return object.__setattr__(self, attr, value)

        aClass.__getattribute__ = getattributes
        aClass.__setattr__ = setattributes           # 접근자 추가
        return aClass                                # 원래 클래스 반환
    return onDecorator
