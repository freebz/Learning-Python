# 존재하지 않는 키에 대한 에러 피하기

if (2, 3, 6) in Matrix:         # 값을 가져오기 전에 키가 있는지 검사
    print(Matrix[(2, 3, 6)])    # if/else에 대해서는 10장과 12장 참조
else:
    print(0)

# 0
try:
    print(Matrix[(2, 3, 6)])    # 인덱스 try
except KeyError:                # 에러 처리
    print(0)                    # tyr/except에 대해서는 10장과 34장 참조

# 0
Matrix.get((2, 3, 4), 0)        # 존재할 경우: 값을 가져와서 반환
# 88
Matrix.get((2, 3, 6), 0)        # 존재하지 않을 경우: 기본 인수 사용
# 0
