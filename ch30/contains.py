# -*- coding: utf-8 -*-
# contains.py 파일
from __future__ import print_function    # 2.X/3.X 호환성

class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):            # 반복을 위한 폴백 함수
        print('get[%s]:' % i, end='')    # 인덱스와 슬라이스를 위해서도 사용
        return self.data[i]

    def __iter__(self):                  # 반복에서 선호되는 방식
        print('iter=> ', end='')         # 오직 하나의 활성화된 반복자만 허용
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):           # 'in'에서 선호되는 방식
        print('contains: ', end='')
        return x in self.data
    next = __next__                      # 2.X/3.X 호환성 유지

if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])           # 인스턴스 생성
    print(3 in X) # Membership
    for i in X: # for loops
        print(i, end=' | ')

    print()
    print([i ** 2 for i in X])           # 다른 반복 맥락
    print( list(map(bin, X)) )

    I = iter(X)                          # 직접 반복(다른 맥락에서 수행하는 것과 동일)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
