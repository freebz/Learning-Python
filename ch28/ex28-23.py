# 단계 7(최종): 객체를 데이터베이스에 저장하기

# 셸브 데이터베이스에 객체 저장하기

import person                   # import로 클래스 적재
bob = person.Person(...)        # 모듈 이름을 통해 감

from person import Person       # from으로 클래스 적재
bob = Person(...)               # 이름을 직접 사용함


# makedb.py 파일: Person 객체를 셸브 데이터베이스에 저장

from person import Person, Manager               # 우리 클래스들을 적재
bob = Person('Bob Smith')                        # 저장될 객체들을 재생성
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')                     # 객체가 저장될 파일 이름
for obj in (bob, sue, tom):                      # 객체의 이름 속성을 키로 사용
    db[obj.name] = obj                           # 객체를 키에 의해 셸브에 저장
db.close()                                       # 변경이 완료되면 닫기
