# JSON 형식의 파이썬 객체를 저장하기

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
rec
# {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}


import json
json.dumps(rec)
# '{"name": {"first": "Bob", "last": "Smith"}, "job": ["dev", "mgr"], "age": 40.5}'

S = json.dumps(rec)
S
# '{"name": {"first": "Bob", "last": "Smith"}, "job": ["dev", "mgr"], "age": 40.5}'

O = json.loads(S)
O
# {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}
O == rec
# True


json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())
# {
#     "name": {
#         "first": "Bob",
#         "last": "Smith"
#     },
#     "job": [
#         "dev",
#         "mgr"
#     ],
#     "age": 40.5
# }
P = json.load(open('testjson.txt'))
P
# {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}


import csv
rdr = csv.reader(open('csvdata.txt'))
for row in rdr: print(row)

# ['a', 'bbb', 'cc', 'dddd']
# ['11', '22', '33', '44']
