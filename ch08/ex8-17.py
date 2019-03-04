# 딕셔너리에 중첩하기

rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['job'] = 'developer/manager'

print(rec['name'])
# Bob


rec = {'name': 'Bob',
       'jobs': ['developer', 'manager'],
       'web': 'www.bobs.org/ Bob',
       'home': {'state': 'Overworked', 'zip': 12345}}


rec['name']
# 'Bob'
rec['jobs']
# ['developer', 'manager']
rec['jobs'][1]
# 'manager'
rec['home']['zip']
# 12345


db = []
db.append(rec)                  # 리스트 '데이터베이스'
db.append(other)
db[0]['jobs']

db = {}
db['bob'] = rec                 # 딕셔너리 '데이터베이스'
db['sue'] = other
db['bob']['jobs']
