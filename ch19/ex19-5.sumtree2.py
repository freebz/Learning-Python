# 재귀 vs 큐 그리고 스택

def sumtree(L):                 # 너비 우선, 명시적인 큐
    tot = 0
    items = list(L)             # 최상위 복사본으로 시작
    while items:
        front = items.pop(0)    # 가장 앞의 아이템을 가져오고 삭제
        if not isinstance(front, list):
            tot += front        # 숫자를 직접 더하기
        else:
            items.extend(front) # 중첩된 리스트의 모든 항목 끝에 추가
    return tot


def sumtree(L):                 # 깊이 우선, 명시적인 스택
    tot = 0
    items = list(L)             # 최상위 복사본으로 시작
    while items:
        fornt = items.pop(0)    # 가장 앞의 아이템을 가져오고 삭제
        if not isinstance(front, list):
            tot += front        # 숫자를 직접 더하기
        else:
            items.extend(front) # 중첩된 리스트를 모든 항목을 앞에 추가
    return tot
