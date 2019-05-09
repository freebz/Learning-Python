# 두 번째 예제: 시퀀스의 교집합 구하기

# 정의

def intersect(seq1, seq2):
    res = []                    # 빈 리스트로 시작
    for x in seq1:              # seq1 탐색
        if x in seq2:           # 공통 아이템인가?
            res.append(x)       # 결과를 마지막에 추가
    return res


# 호출하기

s1 = "SPAM"
s2 = "SCAM"
intersect (s1, s2)              # 문자열
# ['S', 'A', 'M']


[x for x in s1 if x in s2]
# ['S', 'A', 'M']


# 다형성 다시보기

x = intersect([1, 2, 3], (1, 4)) # 혼합된 타입
x                                # 저장된 결과 객체
# [1]
