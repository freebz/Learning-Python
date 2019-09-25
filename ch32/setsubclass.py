# -*- coding: utf-8 -*-
from __future__ import print_function    # 2.X 호환성

class Set(list):
    def __init__(self, value = []):      # 생성자
        list.__init__(self)              # list 변경
        self.concat(value)               # 가변 기본값 복사

    def intersect(self, other):          # other는 시퀀스
        res = []                         # self는 대상
        for x in self:
            if x in other:               # 공통 아이템 추출하기
                res.append(x)
        return Set(res)                  # 신규 Set 반환

    def union(self, other):              # other는 시퀀스
        res = Set(self)                  # me와 my list 복사
        res.concat(other)
        return res

    def concat(self, value):             # value: 리스트,집합, 등.
        for x in value:                  # 중복 아이템 제거
            if not x in self:
                self.append(x)

    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return 'Set:' + list.__repr__(self)

if __name__ == '__main__':
    x = Set([1,3,5,7])
    y = Set([2,1,4,5,6])
    print(x, y, len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse(); print(x)
