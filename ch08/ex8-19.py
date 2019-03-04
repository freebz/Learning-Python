# 더 생각해 볼 주제: 딕셔너리 vs 리스트

L = ['Bob', 40.5, ['dev', 'mgr']] # 리스트 기반의 '레코드'
L[0]
# 'Bob'
L[1]                            # 필드 값을 구하기 위한 위치 값
# 40.5
L[2][1]
# 'mgr'


D = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
D['name']
# 'Bob'
D['age']                        # 딕셔너리 기반의 '레코드'
# 40.5
D['jobs'][1]                    # 이름은 숫자 이상의 의미가 있음
# 'mgr'


D = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
D['name']
# 'Bob'
D['jobs'].remove('mgr')
D
# {'name': 'Bob', 'age': 40.5, 'jobs': ['dev']}


D = {}
D['state1'] = True              # 방문 상태를 나타내는 딕셔너리
'state1' in D
# True
S = set()
S.add('state1')                 # 집합으로 구현한 같은 기능
'state1' in S
# True
