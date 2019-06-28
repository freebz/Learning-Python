# 제너레이터 표현식 vs 필터

line = 'aa bbb c'
''.join(x for x in line.split() if len(x) > 1)         # if를 사용한 제너레이터
# 'aabbb'
''.join(filter(lambda x: len(x) > 1, line.split()))    # filter와 유사함
# 'aabbb'


''.join(x.upper() for x in line.split() if len(x) > 1)
# 'AABBB'
''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split())))
# 'AABBB'


''.join(x.upper() for x in line.split() if len(x) > 1)
# 'AABBB'

res = ''
for x in line.split():          # 동등한 문?
    if len(x) > 1:              # join과 같음
        res += x.upper()

res
# 'AABBB'
