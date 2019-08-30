# 생성자와 표현식: __init__과 __sub__

# number.py 파일

class Number:
    def __init__(self, start):              # Number(start)에서
        self.data = start
    def __sub__(self, other):               # 인스턴스-other에서
        return Number(self.data - other)    # 결과는 새로운 인스턴스

from number import Number                   # 모듈로부터 클래스 가져오기
X = Number(5)                               # Number.__init__(X, 5)
Y = X - 2                                   # Number.__sub__(X, 2)
Y.data                                      # Y는 새로운 Number 인스턴스
# 3
