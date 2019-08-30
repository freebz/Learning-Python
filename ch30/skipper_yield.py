# skipper_yield.py 파일

class SkipObject:                       # 또 다른 __iter__ + yield 제너레이터
    def __init__(self, wrapped):        # 일반적으로 인스턴스 범위에 기록됨
        self.wrapped = wrapped          # 지역 범위 상태는 자동으로 저장됨
    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item
