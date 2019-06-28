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
