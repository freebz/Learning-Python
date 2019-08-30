# squares_nonyield.py 파일

class Squares:
    def __init__(self, start, stop): # yield가 없는 제너레이터
        self.start = start           # 다중 스캔: 추가 객체 필요
        self.stop = stop
    def __iter__(self):
        return SquaresIter(self.start, self.stop)

class SquaresIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
