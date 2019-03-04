# 희소 데이터 구조를 위해 딕셔너리 사용하기: 튜플 키

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

X = 2; Y = 3; Z = 4             # ;문들을 구분: 10장 참고
Matrix[(X, Y, Z)]
# 88
Matrix
# {(2, 3, 4): 88, (7, 8, 9): 99}


Matrix[(2,3,6)]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: (2, 3, 6)
