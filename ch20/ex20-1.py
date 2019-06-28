# 리스트 컴프리헨션 vs 맵

ord('s')
# 115


res = []
for x in 'spam':
    res.append(ord(x))          # 수동으로 결과를 수집

res
# [115, 112, 97, 109]


res = list(map(ord, 'spam'))    # 시퀀스에 함수를 적용
res
# [115, 112, 97, 109]


res = [ord(x) for x in 'spam']  # 시퀀스에 표현식을 적용
res
# [115, 112, 97, 109]


[ x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


list(map((lambda x: x ** 2), range(10)))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
