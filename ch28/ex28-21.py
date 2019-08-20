# 도구 클래스에서의 이름 관련 고려 사항

class TopTest(AttrDisplay):
    ...
    def gatherAttrs(self):      # AttrDisplay의 gatherAttrs를 대체
        return 'Spam'
