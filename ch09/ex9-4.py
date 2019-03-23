# 왜 리스트와 튜플이 존재하는가?

# 레코드 다시보기: 명명된 튜플

bob = ('Bob', 40.5, ['dev', 'mgr'])    # 튜플 레코드
bob
# ('Bob', 40.5, ['dev', 'mgr'])

bob[0], bob[2]                         # 위치에 의한 접근
# ('Bob', ['dev', 'mgr'])


bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr']) # 딕셔너리 레코드
bob
# {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}

bob['name'], bob['jobs']        # 키로 접근
# ('Bob', ['dev', 'mgr'])


tuple(bob.values())             # 값을 튜플로 변환
# ('Bob', 40.5, ['dev', 'mgr'])
list(bob.items())               # 튜플 항목들로 변환된 리스트
# [('name', 'Bob'), ('age', 40.5), ('jobs', ['dev', 'mgr'])]


from collections import namedtuple               # 확장 타입 임포트
Rec = namedtuple('Rec', ['name', 'age', 'jobs']) # 생성된 클래스 만들기
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])  # 명명된 튜플 레코드
bob
# Rec(name='Bob', age=40.5, jobs=['dev', 'mgr'])

bob[0], bob[2]                                   # 위치로 접근
# ('Bob', ['dev', 'mgr'])
bob.name, bob.jobs                               # 속성으로 접근
# ('Bob', ['dev', 'mgr'])


O = bob._asdict()               # 딕셔너리와 유사한 형식
O['name'], O['jobs']            # 키로 접근도 가능
# ('Bob', ['dev', 'mgr'])
O
# OrderedDict([('name', 'Bob'), ('age', 40.5), ('jobs', ['dev', 'mgr'])])


bob = Rec('Bob', 40.5, ['dev', 'mgr']) # 튜플과 명명된 튜플 모두
name, age, jobs = bob                  # 지원하는 튜플 할당(11장)
name, jobs
# ('Bob', ['dev', 'mgr'])

for x in bob: print(x)          # 반복 상황(14, 20장)
# ...Bob, 40.5, ['dev', 'mgr'] 출력...


bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
job, name, age = bob.values()
name, job                       # Dict와 같음(그러나 순서는 다를 수 있다)
# ('Bob', ['dev', 'mgr'])

for x in bob: print(bob[x])     # 인덱스 값인 키를 통한 단계
# ...값 출력...
for x in bob.values(): print(x) # 값 뷰를 통한 단계
# ...값 출력...
