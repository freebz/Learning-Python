# 중첩 다시 보기

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}


rec['name']                     # 'name'은 중첩된 딕셔너리
# {'first': 'Bob', 'last': 'Smith'}

rec['name']['last']             # 중첩된 딕셔너리 인덱스
# 'Smith'

rec['jobs']                     # 'jobs'는 중첩된 리스트
# ['dev', 'mgr']
rec['jobs'][-1]                 # 중첩된 리스트 인덱스
# 'mgr'

rec['jobs'].append('janitor')   # Bob의 작업 설명을 확장
rec
# {'name': {'first': 'Bob', 'last': 'Smith'}, 'jobs': ['dev', 'mgr', 'janitor'], 'age': 40.5}
