# 인덱싱과 슬라이싱: __getitem__과 __setitem__

class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
X[2]                            # X[i]는 X.__getitem__(i)를 호출
# 4

for i in range(5):
    print(X[i], end=' ')        # 매번 __getitem__(x, I)를 실행

# 0 1 4 9 16
