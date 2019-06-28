# 자신만의 map(func, ...)을 작성하기

# map(함수, 시퀀스들...)은 zip과 많이 유사함

def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))


# [2, 1, 0, 1, 2]
# [1, 8, 81]


# 리스트 컴프리헨션 사용하기

def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))


# 제너레이터 사용하기: yield and (...)

def mymap(func, *seqs):
    res = []
    for args in zip(seqs):
        yield func(*args)

def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))


print(list(mymap(abs, [-2, -1, 0, 1, 2])))
print(list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])))
