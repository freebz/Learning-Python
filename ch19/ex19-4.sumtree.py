# 임의 구조 처리하기

[1, [2, [3, 4], 5], 6, [7, 8]]  # 임의의 중첩된 서브리스트


# sumtree.py 파일

def sumtree(L):
    tot = 0
    for x in L:                 # 현재 단계의 각 아이템에 대한 반복
        if not isinstance(x, list):
            tot += x            # 숫자를 직접 더하기
        else:
            tot += sumtree(x)   # 서브리스트에 대한 재귀
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]] # 임의의 중첩
print(sumtree(L))                  # 36 출력

# 매우 복잡한 경우
print(sumtree([1, [2, [3, [4, [5]]]]])) # 15 출력(오른쪽이 무거움)
print(sumtree([[[[[1], 2], 3], 4], 5])) # 15 출력(왼쪽이 무거움)
