# -*- coding: utf-8 -*-
# number.py 파일

class Number:
    def __init__(self, start):              # Number(start)에서
        self.data = start
    def __sub__(self, other):               # 인스턴스-other에서
        return Number(self.data - other)    # 결과는 새로운 인스턴스
