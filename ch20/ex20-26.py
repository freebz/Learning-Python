# 예제: 반복 도구를 이용하여 zip과 map 흉내 내기

S1 = 'abc'
S2 = 'xyz123'
list(zip(S1, S2))               # zip은 반복 객체들로부터 아이템들을 짝지음
# [('a', 'x'), ('b', 'y'), ('c', 'z')]

# zip은 아이템들을 짝짓고, 짧은 반복 객체를 기준으로 자름
list(zip([-2, -1, 0, 1, 2]))    # 단일 시퀀스: 하나로 구성된 튜플들
# [(-2,), (-1,), (0,), (1,), (2,)]
list(zip([1, 2, 3], [2, 3, 4, 5])) # N개 시퀀스: N개로 구성된 튜플들
# [(1, 2), (2, 3), (3, 4)]

# map은 짝지어진 아이템들을 함수로 전달하고, 짧은 반복 객체를 기준으로 자름
list(map(abs, [-2, -1, 0, 1, 2])) # 단일 시퀀스: 한 개의 인수 함수
# [2, 1, 0, 1, 2]
list(map(pow, [1, 2, 3], [2, 3, 4, 5])) # N개 시퀀스: N개의 인수 함수. 3.X
# [1, 8, 81]

# map과 zip은 임의의 반복 객체들을 받아들임
list(map(lambda x, y: x + y, open('script2.py'), open('script2.py')))
# ['import sys\nimport sys\n', 'print(sys.path)\nprint(sys.path)\n', ...등등...]

[x + y for (x, y) in zip(open('script2.py'), open('script2.py'))]
# ['import sys\nimport sys\n', 'print(sys.path)\nprint(sys.path)\n', ...등등...]
