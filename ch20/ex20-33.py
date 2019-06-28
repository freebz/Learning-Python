# 집합과 딕션너리를 위한 확장된 컴프리헨션 구문

[x * x for x in range(10) if x % 2 == 0]      # 리스트는 정렬됨
# [0, 4, 16, 36, 64]
{x * x for x in range(10) if x % 2 == 0}      # 집합은 정렬되지 않음
# {0, 64, 4, 36, 16}
{x: x * x for x in range(10) if x % 2 == 0}   # 딕셔너리 키 또한 정렬되지 않음
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


[x + y for x in [1, 2, 3] for y in [4, 5, 6]] # 리스트는 중복을 허용함
# [5, 6, 7, 6, 7, 8, 7, 8, 9]
{x + y for x in [1, 2, 3] for y in [4, 5, 6]} # 집합은 중복을 허용하지 않음
# {5, 6, 7, 8, 9}
{x: y for x in [1, 2, 3] for y in [4, 5, 6]}  # 딕셔너리 키 또한 중복을 허용하지 않음
# {1: 6, 2: 6, 3: 6}


{x + y for x in 'ab' for y in 'cd'}
# {'ad', 'bd', 'ac', 'bc'}

{x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'}
# {'ac': (97, 99), 'ad': (97, 100), 'bc': (98, 99), 'bd': (98, 100)}

{k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'}
# {'sausagesausage', 'spamspam'}

{k.upper(): k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'}
# {'SPAM': 'spamspam', 'SAUSAGE': 'sausagesausage'}
