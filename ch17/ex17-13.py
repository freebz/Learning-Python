# 루프 변수는 범위가 아니라 기본 인수가 필요

def makeActions():
    acts = []
    for i in range(5):                   # 각각의 i를 기억하고자 함
        acts.append(lambda x: i ** x)    # 하지만 모두 동일한 i를 기억
    return acts

acts = makeActions()
acts[0]
# <function makeActions.<locals>.<lambda> at 0x7fe298596730>


acts[0](2)                      # 모두 4 ** 2 값을 반환함. 4: 마지막 i값
# 16
acts[1](2)                      # 예상대로라면 1 ** 2 (1)
# 16
acts[2](2)                      # 예상대로라면 2 ** 2 (4)
# 16
acts[4](2)                      # 예상대로라면 여기서만 4 ** 2 (16)이 반환되어야 함
# 16


def makeActions():
    acts = []
    for i in range(5):                        # 기본 인수를 사용
        acts.append(lambda x, i=i: i ** x)    # 현재 i 값을 기억
    return acts

acts = makeActions()
acts[0](2)                      # 0 ** 2
# 0
acts[1](2)                      # 1 ** 2
# 1
acts[2](2)                      # 2 ** 2
# 4
acts[4](2)                      # 4 ** 2
# 16
