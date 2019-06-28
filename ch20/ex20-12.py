# 제너레이터 함수 vs 제너레이터 표현식

G = (c * 4 for c in 'SPAM')     # 제너레이터 표현식
list(G)                         # 제너레이터가 모든 결과를 생성하도록 강제함
# ['SSSS', 'PPPP', 'AAAA', 'MMMM']


def timesfour(S):                # 제너레이터 함수
    for c in S:
        yield c * 4

G = timesfour('spam')
list(G)                         # 자동 반복
# ['ssss', 'pppp', 'aaaa', 'mmmm']


G = (c * 4 for c in 'SPAM')
I = iter(G)                     # 수동 반복(표현식)
next(I)
# 'SSSS'
next(I)
# 'PPPP'

G = timesfour('spam')
I = iter(G)                     # 수동 반복(함수)
next(I)
# 'ssss'
next(I)
# 'pppp'


line = 'aa bbb c'

''.join(x.upper() for x in line.split() if len(x) > 1)    # 표현식
# 'AABBB'

def gensub(line):                                         # 함수
    for x in line.split():
        if len(x) > 1:
            yield x.upper()

''.join(gensub(line))           # 그러나 제너레이터를 사용해야 하는 이유는 무엇인가?
# 'AABBB'
