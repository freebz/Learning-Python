# 순열(permutation): 모든 가능한 조합

# permute.py 파일
def permute1(seq):
    if not seq:                               # 모든 시퀀스 섞기: 리스트
        return [seq]                          # 빈 시퀀스
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]        # 현재 노드 삭제
            for x in permute1(rest):          # 나머지들의 순열
                res.append(seq[i:i+1] + x)    # 앞쪽에 노드 추가
        return res

def permute2(seq):
    if not seq:                               # 모든 시퀀스 섞기: 제너레이터
        yield seq                             # 빈 시퀀스
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]        # 현재 노드 삭제
            for x in permute2(rest):          # 나머지들의 순열
                yield seq[i:i+1] + x          # 앞쪽에 노드 추가


from scramble import scramble
from permute import permute1, permute2

list(scramble('abc'))           # 단순 뒤섞기: N
# ['abc', 'bca', 'cab']

permute1('abc')                 # 가장 큰 순열: N
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
list(permute2('abc'))           # 모든 조합 생성
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

G = permute2('abc')             # 반복(iter()는 불필요함)
next(G)
# 'abc'
next(G)
# 'acb'
for x in permute2('abc'): print (x) # 자동 반복
# ...6 라인 출력...


permute1('spam') == list(permute2('spam'))
# True
len(list(permute2('spam'))), len(list(scramble('spam')))
# (24, 4)

list(scramble('spam'))
# ['spam', 'pams', 'amsp', 'mspa']
list(permute2('spam'))
# ['spam', 'spma', 'sapm', 'samp', 'smpa', 'smap', 'psam', 'psma', 'pasm', 'pams', 'pmsa', 'pmas', 'aspm', 'asmp', 'apsm', 'apms', 'amsp', 'amps', 'mspa', 'msap', 'mpsa', 'mpas', 'masp', 'maps']
