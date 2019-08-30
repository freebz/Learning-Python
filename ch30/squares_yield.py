# squares_yield.py 파일

class Squares:                          # __iter__ + yield 제너레이터
    def __init__(self, start, stop):    # __next__는 자동으로/암묵적으로 존재
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
