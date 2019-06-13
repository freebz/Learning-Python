# 함수형 프로그래밍 도구

# 반복 객체에 대해 함수 적용하기: map

counters = [1, 2, 3, 4]

updated = []
for x in counters:
    updated.append(x + 10)      # 각 아이템에 10 더하기

updated
# [11, 12, 13, 14]


def inc(x): return x + 10       # 실행될 함수

list(map(inc, counters))        # 결과 수집
# [11, 12, 13, 14]


list(map((lambda x: x + 3), counters)) # 함수 표현식
# [4, 5, 6, 7]


def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res


list(map(inc, [1, 2, 3]))       # 내장된 map은 반복 객체
# [11, 12, 13]
mymap(inc, [1, 2, 3])           # 직접 만든 함수는 리스트를 반환(제너레이터 참고)
# [11, 12, 13]


pow(3, 4)                       # 3 ** 4
# 81
list(map(pow, [1, 2, 3], [2, 3, 4])) # 1 ** 2, 2 ** 3, 3 ** 4
# [1, 8, 81]


list(map(inc, [1, 2, 3, 4]))
# [11, 12, 13, 14]
[inc(x) for x in [1, 2, 3, 4]]  # 대신 () 괄호를 사용하면 제너레이터 반환
# [11, 12, 13, 14]
