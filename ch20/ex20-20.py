# 간단한 함수

def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res

scramble('spam')
# ['spam', 'pams', 'amsp', 'mspa']

def scramble(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]

scramble('spam')
# ['spam', 'pams', 'amsp', 'mspa']

for x in scramble((1, 2, 3)):
    print(x, end=' ')

# (1, 2, 3) (2, 3, 1) (3, 1, 2)
