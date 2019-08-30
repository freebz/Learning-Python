class Squares:                          # __iter__에 대응하는 것이 없음(squares_manual.py)
    def __init__(self, start, stop):    # __next__는 자동으로/암묵적으로 존재
        self.start = start
        self.stop = stop
    def gen(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
