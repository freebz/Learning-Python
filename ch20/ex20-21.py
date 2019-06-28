# 제너레이터 함수

def scramble(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1] # 제너레이터 함수는
        yield seq               # 여기서 지정됨

def scramble(seq):
    for i in range(len(seq)):   # 제너레이터 함수는
        yield seq[i:] + seq[:i] # 반복마다 하나의 아이템을 산출함

list(scramble('spam'))          # list()는 모든 결과 생성
# ['spam', 'pams', 'amsp', 'mspa']
list(scramble((1, 2, 3)))       # 모든 시퀀스 타입이 동작함
# [(1, 2, 3), (2, 3, 1), (3, 1, 2)]

for x in scramble((1, 2, 3)):   # for 루프는 결과를 생성함
    print(x, end=' ')

# (1, 2, 3) (2, 3, 1) (3, 1, 2)
