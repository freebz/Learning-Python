# 서브클래싱으로 타입 확장하기

# 내장된 리스트 타입/클래스를 서브클래스로 만들기
# 1..N을 0..N-1로 매핑하기: 내장된 버전을 다시 호출

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)

if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')           # __init__는 list로부터 상속받음
    print(x)                    # __repr__은 list로부터 상속받음

    print(x[1])                 # MyList.__getitem__
    print(x[3])                 # list 슈퍼클래스의 메서드를 변경

    x.append('spam'); print(x)  # list 슈퍼클래스의 속성
    x.reverse();      print(x)


# python typesubclass.py 
# ['a', 'b', 'c']
# ['a', 'b', 'c']
# (indexing ['a', 'b', 'c'] at 1)
# a
# (indexing ['a', 'b', 'c'] at 3)
# c
# ['a', 'b', 'c', 'spam']
# ['spam', 'c', 'b', 'a']


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


# python setsubclass.py
# Set:[1, 3, 5, 7] Set:[2, 1, 4, 5, 6] 4
# Set:[1, 5] Set:[2, 1, 4, 5, 6, 3, 7]
# Set:[1, 5] Set:[1, 3, 5, 7, 2, 4, 6]
# Set:[7, 5, 3, 1]
