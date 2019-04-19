# 중첩된 for 루프

items = ["aaa", 111, (4, 5), 2.01]    # 객체 세트
tests = [(4, 5), 3.14]                # 검색할 키

for key in tests:                     # 모든 키에 대해
    for item in items:                # 모든 아이템에 대해
        if item == key:               # 매칭 테스트
            print(key, "was found")
            break
    else:
        print(key, "not found!")

# (4, 5) was found
# 3.14 not found!


for key in tests:                     # 모든 키에 대해
    if key in items:                  # 파이썬이 매칭을 찾도록 함
        print(key, "was found")
    else:
        print(key, "not found!")

# (4, 5) was found
# 3.14 not found!


seq1 = "spam"
seq2 = "scam"

res = []                        # 빈 리스트
for x in seq1:                  # 첫 번째 시퀀스 탐색
    if x in seq2:               # 공통된 아이템인가?
        res.append(x)           # 최종 결과에 추가

res
# ['s', 'a', 'm']


[x for x in seq1 if x in seq2]  # 파이썬이 결과를 수집하도록 함
# ['s', 'a', 'm']
