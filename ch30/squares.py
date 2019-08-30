# squares.py 파일

class Squares:
    def __init__(self, start, stop):    # 생성될 때 상태 정보 저장
        self.value = start - 1
        self.stop = stop
    def __iter__(self):                 # iter 호출 시, 반복자 객체 가져오기
        return self
    def __next__(self):                 # 매 반복 때마다 제곱값 반환
        if self.value == self.stop:     # 또한 내장된 next에 의해 호출됨
            raise StopIteration
        self.value += 1
        return self.value ** 2
