# 키 정렬: 루프 이용

D = {'a': 1, 'b': 2, 'c': 3}
D
# {'a': 1, 'b': 2, 'c': 3}


Ks = list(D.keys())             # 정렬되지 않은 키 리스트
Ks                              # 2.X에서는 리스트, 3.X에서는 뷰(view)이므로 list()를 사용해야 함
# ['a', 'b', 'c']

Ks.sort()                       # 정렬된 키 리스트
Ks
# ['a', 'b', 'c']

for key in Ks:                  # 정렬된 키를 반복
    print(key, '=>', D[key])    # 여기서 엔터 두 번 입력(3.X.print)

# a => 1
# b => 2
# c => 3


D
# {'a': 1, 'b': 2, 'c': 3}

for key in sorted(D):
    print(key, '=>', D[key])

# a => 1
# b => 2
# c => 3


for c in 'spam':
    print(c.upper())

# S
# P
# A
# M


x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

# spam!spam!spam!spam!
# spam!spam!spam!
# spam!spam!
# spam!
