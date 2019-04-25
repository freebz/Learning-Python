# 수동 반복

L = [1, 2, 3]

for X in L:                     # 자동 반복은
    print(X ** 2, end=' ')      # 반복자를 얻고, __next__를 호출하고 예외를 처리함

# 1 4 9

I = iter(L)                     # 수동 반복: for 루프가 실제 하는 일
while True:
    try:                        # 예외 처리
        X = next(I)             # 또는 3.X에서 I.__next-_
    except StopIteration:
        break
    print(X ** 2, end=' ')

# 1 4 9
