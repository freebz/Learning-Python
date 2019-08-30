# 인덱스 반복: __getitem__

class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]

X = StepperIndex()              # X는 StepperIndex 객체
X.data = "Spam"
X[1]                            # 인덱싱은 __getitem__을 호출
# 'p'
for item in X:                  # for 루프는 __getitem__을 호출
    print(item, end=' ')        # for는 아이템0..N까지 색인

# S p a m


'p' in X                        # 모두 __getitem__을 호출
# True

[c for c in X]                  # 리스트 컴프리헨션
# ['S', 'p', 'a', 'm']

(a, b, c, d) = X                # 시퀀스 할당
a, c, d
# ('S', 'a', 'm')

list(X), tuple(X), ''.join(X)   # 등등...
# (['S', 'p', 'a', 'm'], ('S', 'p', 'a', 'm'), 'Spam')

X
# <__main__.StepperIndex object at 0x7fa8ff29b2e8>
