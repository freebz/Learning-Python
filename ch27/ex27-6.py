# 레코드 다시 살펴보기: 클래스 vs 딕셔너리

rec = ('Bob', 40.5, ['dev', 'mgr']) # 튜플 기반 레코드
print(rec[0])
# Bob

rec = {}
rec['name'] = 'Bob'             # 딕셔너리 기반 레코드
rec['age'] = 40.5               # Or (...), dict(n=v), etc
rec['jobs'] = ['dev', 'mrg']

print(rec['name'])
# Bob


class rec: pass

rec.name = 'Bob'                # 클래스 기반 레코드
rec.age = 40.5
rec.jobs = ['dev', 'mgr']

print(rec.name)
# Bob


class rec: pass

pers1 = rec()                   # 인스턴스 기반 레코드
pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5

pers2 = rec()
pers2.name = 'Sue'
pers2.jobs = ['dev', 'cto']

pers1.name, pers2.name
# ('Bob', 'Sue')


class Person:
    def __init__(self, name, jobs, age=None): # 클래스 = 데이터 + 로직
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self):
        return (self.name, self.jobs)

rec1 = Person('Bob', ['dev', 'mrg'], 40.5) # 생성자 호출
rec2 = Person('Sue', ['dev', 'cto'])

rec1.jobs, rec2.info()     # 속성 + 메서드
# (['dev', 'mrg'], ('Sue', ['dev', 'cto']))


rec = dict(name='Bob', age=40.5, jobs=['dev', 'mgr']) # 딕셔너리

rec = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}

rec = Rec('Bob', 40.5, ['dev', 'mgr']) # 명명된 튜플
