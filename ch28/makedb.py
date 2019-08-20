# -*- coding: utf-8 -*-
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
