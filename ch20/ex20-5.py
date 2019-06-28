# 리스트 컴프리헨션을 남용하지 않도록 하자: KISS

# 또 다른 관점: 성능, 간결함, 표현력

# 더 생각해 볼 주제: 리스트 컴프리헨션과 맵

open('myfile').readlines()
# ['aaa\n', 'bbb\n', 'ccc\n']


[line.rstrip() for line in open('myfile').readlines()]
# ['aaa', 'bbb', 'ccc']

[line.rstrip() for line in open('myfile')]
# ['aaa', 'bbb', 'ccc']

list(map((lambda line: line.rstrip()), open('myfile')))
# ['aaa', 'bbb', 'ccc']


listoftuple = [('bob', 35, 'mgr'), ('sue', 40, 'dev')]


[age for (name, age, job) in listoftuple]
# [35, 40]

list(map((lambda row: row[1]), listoftuple))
# [35, 40]


# 2.X에서
list(map((lambda (name, age, job): age), listoftuple))
# [35, 40]
