# 멤버십: __contains__, __iter__, __getitem__

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


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):            # 반복을 위한 폴백 함수
        print('get[%s]:' % i, end='')    # 인덱스와 슬라이스를 위해서도 사용
        return self.data[i]

    def __iter__(self):                  # 반복을 위해 선호되는 함수
        print('iter=> next:', end='')    # 다중 활성화된 반복자를 허용
        for x in self.data:              # 다음 항목에 대한 별칭(에일리어스)인 __next__가 없음
            yield x
            print('next:', end='')

    def __contains__(self, x):           # 'in'을 위해 선호되는 함수
        print('contains: ', end='')
        return x in self.data


# contains: True
# iter=> next:1 | next:2 | next:3 | next:4 | next:5 | next:
# iter=> next:next:next:next:next:next:[1, 4, 9, 16, 25]
# iter=> next:next:next:next:next:next:['0b1', '0b10', '0b11', '0b100', '0b101']
# iter=> next:1 @ next:2 @ next:3 @ next:4 @ next:5 @ next:


# iter=> next:next:next:True
# iter=> next:1 | next:2 | next:3 | next:4 | next:5 | next:
# iter=> next:next:next:next:next:next:[1, 4, 9, 16, 25]
# iter=> next:next:next:next:next:next:['0b1', '0b10', '0b11', '0b100', '0b101']
# iter=> next:1 @ next:2 @ next:3 @ next:4 @ next:5 @ next:


# get[0]:get[1]:get[2]:True
# get[0]:1 | get[1]:2 | get[2]:3 | get[3]:4 | get[4]:5 | get[5]:
# get[0]:get[1]:get[2]:get[3]:get[4]:get[5]:[1, 4, 9, 16, 25]
# get[0]:get[1]:get[2]:get[3]:get[4]:get[5]:['0b1', '0b10', '0b11', '0b100', '0b101']
# get[0]:1 @ get[1]:2 @ get[2]:3 @ get[3]:4 @ get[4]:5 @ get[5]:


from contains import Iters
X = Iters('spam')               # 인덱싱
X[0]                            # __getitem__(0)
# get[0]:'s'

'spam'[1:]                      # 슬라이스 구문
# 'pam'
'spam'[slice(1, None)]          # 슬라이스 객체
# 'pam'

X[1:]                           # __getitem__(slice(..))
# get[slice(1, None, None)]:'pam'
X[:-1]
# get[slice(None, -1, None)]:'spa'

list(X)                         # 그리고 반복 도구
# iter=> next:next:next:next:next:['s', 'p', 'a', 'm']
