# 슬라이스 가로채기

L = [5, 6, 7, 8, 9]
L[2:4]                          # 슬라이스 구문을 이용한 슬라이스 2..(4-1)
# [7, 8]
L[1:]
# [6, 7, 8, 9]
L[:-1]
# [5, 6, 7, 8]
L[::2]
# [5, 7, 9]


L[slice(2, 4)]                  # 슬라이스 객체를 이용한 슬라이스
# [7, 8]
L[slice(1, None)]
# [6, 7, 8, 9]
L[slice(None, -1)]
# [5, 6, 7, 8]
L[slice(None, None, 2)]
# [5, 7, 9]


class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):     # 인덱스 또는 슬라이스를 위해 호출
        print('getitem:', index)
        return self.data[index]       # 인덱스 또는 슬라이스 실행

X = Indexer()
X[0]                                  # 인덱싱은 __getitem__에 정수를 보냄
# getitem: 0
# 5
X[1]
# getitem: 1
# 6
X[-1]
# getitem: -1
# 9


X[2:4]                          # 슬라이싱은 __getitem__에 슬라이스 객체를 전달
# getitem: slice(2, 4, None)
# [7, 8]
X[1:]
# getitem: slice(1, None, None)
# [6, 7, 8, 9]
X[:-1]
# getitem: slice(None, -1, None)
# [5, 6, 7, 8]
X[::2]
# getitem: slice(None, None, 2)
# [5, 7, 9]


class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):         # 사용 방식 테스트
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)
X = Indexer()
X[99]
# indexing 99
X[1:99:2]
# slicing 1 99 2
X[1:]
# slicing 1 None None


class IndexSetter:
    def __setitem__(self, index, value):    # 인덱스와 슬라이스 할당 가로챔
        ...
        self.data[index] = value            # 인덱스 또는 슬라이스 할당
