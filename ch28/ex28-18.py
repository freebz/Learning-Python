# 단계 6: 내부 검사 도구 사용하기

from person import Person
bob = Person('Bob Smith')
bob                             # bob의 __repr__(__str__이 아니라)을 보여줌
# [Person: Bob Smith, 0]
print(bob)                      # 위와 같음: print => __str__ 또는 __repr__
# [Person: Bob Smith, 0]

bob.__class__                   # bob의 class와 그 이름을 보여 줌
# <class 'person.Person'>
bob.__class__.__name__
# 'Person'

list(bob.__dict__.keys())       # 속성은 실제로 딕셔너리의 키임
# ['name', 'job', 'pay']        # 3.X에서 리스트로 구성하기 위해 list 사용

for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key])    # 수동으로 인덱스
    
# name => Bob Smith
# job => None
# pay => 0

for key in bob.__dict__:
    print(key, '=>', getattr(bob, key))    # obj.attr, 하지만 attr은 변수

# name => Bob Smith
# job => None
# pay => 0
