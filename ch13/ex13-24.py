# zip을 이용한 딕셔너리 구성

D1 = {'spam':1, 'eggs':3, 'toast':5}
D1
# {'spam': 1, 'eggs': 3, 'toast': 5}

D1 = {}
D1['spam'] = 1
D1['eggs'] = 3
D1['toast'] = 5


keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]


list(zip(keys, vals))
# [('spam', 1), ('eggs', 3), ('toast', 5)]

D2 = {}
for (k, v) in zip(keys, vals): D2[k] = v

D2
# {'spam': 1, 'eggs': 3, 'toast': 5}


keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]

D3 = dict(zip(keys, vals))
D3
# {'spam': 1, 'eggs': 3, 'toast': 5}


{k: v for (k, v) in zip(keys, vals)}
# {'spam': 1, 'eggs': 3, 'toast': 5}
