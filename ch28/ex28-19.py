# 일반적인 디스플레이 도구

# classtools.py(새로 변경한 버전) 파일
"여러 가지 클래스 유틸리티와 도구들"

class AttrDisplay:
    """
    상속 가능한 디스플레이 오버로드 메서드를 제공
    이 메서드는 인스턴스를 이들의 클래스 이름과 함께 그 인스턴스에 저장된 각 속성을 이름 = 쌍으로 보여 줌
    (하지만 그 인스턴스의 클래스로부터 상속받은 속성을 보여 주지는 않음)
    어떤 클래스에도 혼합될 수 있으며, 어떤 인스턴스에서도 동작함
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__ == '__main__':

    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2
    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()         # 두 인스턴스를 생성
    print(X)                            # 모든 인스턴스 속성들을 보여 줌
    print(Y)                            # 가장 낮은 클래스 이름을 보여 줌


# python classtools.py
# [TopTest: attr1=0, attr2=1]
# [SubTest: attr1=2, attr2=3]
