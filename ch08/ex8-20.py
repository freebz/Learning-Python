# 파이썬 3.X와 2.7에서 딕셔너리의 변경된 사항

# 3.X와 2.7에서의 딕셔너리 컴프리헨션

list(zip(['a', 'b', 'c'], [1, 2, 3])) # 키와 값을 함께 묶기
# [('a', 1), ('b', 2), ('c', 3)]

D = dict(zip(['a', 'b', 'c'], [1, 2, 3])) # zip 결과로 딕셔너리 만들기
D
# {'a': 1, 'b': 2, 'c': 3}


D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
D
# {'a': 1, 'b': 2, 'c': 3}


D = {x: x ** 2 for x in [1, 2, 3, 4]} # 또는: range(1, 5)
D
# {1: 1, 2: 4, 3: 9, 4: 16}

D = {c: c * 4 for c in 'SPAM'}  # 모든 가변 객체에 대해 루프를 돌 수 있음
D
# {'S': 'SSSS', 'P': 'PPPP', 'A': 'AAAA', 'M': 'MMMM'}

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
D
# {'spam': 'SPAM!', 'eggs': 'EGGS!', 'ham': 'HAM!'}


D = dict.fromkeys(['a', 'b', 'c'], 0) # 키로부터 딕셔너리 초기화
D
# {'a': 0, 'b': 0, 'c': 0}

D = {k:0 for k in ['a', 'b', 'c']} # 컴프리헨션을 이용한 같은 초기화
D
# {'a': 0, 'b': 0, 'c': 0}

D = dict.fromkeys('spam')       # 가변 객체에 기본값을 설정하는 방법
D
# {'s': None, 'p': None, 'a': None, 'm': None}

D = {k: None for k in 'spam'}
D
# {'s': None, 'p': None, 'a': None, 'm': None}
