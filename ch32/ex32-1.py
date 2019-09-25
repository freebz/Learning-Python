# 내장된 타입 확장하기

# 임베딩으로 타입 확장하기

class Set:
    def __init__(self, value = []):     # 생성자
        self.data = []                  # 리스트 관리
        self.concat(value)

    def intersect(self, other):         # other는 시퀀스
        res = []                        # self가 대상
        for x in self.data:
            if x in other:              # 중복 아이템 선택
                res.append(x)
        return Set(res)                 # 신규 집합 반환

    def union(self, other):             # other는 시퀀스
        res = self.data[:]              # my list의 사본
        for x in other:                 # other에 아이템 추가
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):            # value: 리스트, 집합...
        for x in value:                 # 중복 삭제
            if not x in self.data:
                self.data.append(x)

    def __len__(self): return len(self.data)                # self면, len(self)
    def __getitem__(self, key): return self.data[key]       # self[i], self[i:j]
    def __and__(self, other): return self.intersect(other)  # self & other
    def __or__(self, other): return self.union(other)       # self | other
    def __repr__(self): return 'Set:' + repr(self.data)     # print(self)....
    def __iter__(self): return iter(self.data)              # for x in self....


from setwrapper import Set
x = Set([1, 3, 5, 7])
print(x.union(Set([1, 4, 7])))          # 집합 [1, 3, 5, 7, 4]을 출력
print(x | Set([1, 4, 6]))               # 집합 [1, 3, 5, 7, 4, 6]을 출력
