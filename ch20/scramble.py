# file scramble.py

def scramble(seq):
    for i in range(len(seq)):   # 제너레이터 함수는
        yield seq[i:] + seq[:i] # 반복마다 하나의 아이템을 산출함

scramble2 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
