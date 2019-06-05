def intersect(*args):
    res = []
    for x in args[0]:                   # 첫 번째 시퀀스 탐색
        if x in res: continue           # 중복 항목은 건너뜀
        for other in args[1:]:          # 다른 인수들을 위하여
            if x not in other: break    # 각각의 인수에 해당 항목이 있는지?
        else:                           # 없으면: 루프 빠져나가기
            res.append(x)               # 있으면: 마지막에 항목 추가
    return res

def union(*args):
    res = []
    for seq in args:                    # 모든 인수를 위해
        for x in seq:                   # 모든 항목을 위해
            if not x in res:
                res.append(x)           # 새로운 항목을 결과에 추가
    return res
