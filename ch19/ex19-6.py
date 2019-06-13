# 순환, 경로 그리고 스택 제한

if state not in visited:
    visited.add(state)          # x.add(state), x[state] = True 또는 x.append(state)
    ...계속 진행...


visited.add(front)
...계속 진행...
items.extend([x for x in front if x not in visited])


sys.getrecursionlimit()         # 기본값 1000
# 1000
sys.setrecursionlimit(10000)    # 더 많이 중첩할 수 있도록 설정
help(sys.setrecursionlimit)     # 함수에 대한 추가적인 정보 보기
