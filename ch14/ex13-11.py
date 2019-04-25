# 중첩된 루프: for

[x + y for x in 'abc' for y in 'lmn']
# ['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']


res = []
for x in 'abc':
    for y in 'lmn':
        res.append(x + y)

res
# ['al', 'am', 'an', 'bl', 'bm', 'bn', 'cl', 'cm', 'cn']
