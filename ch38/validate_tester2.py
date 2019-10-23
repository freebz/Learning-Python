# validate_tester2.py 파일
from __future__ import print_function             # 2.X 호환성

from validate_tester import loadclass
CardHolder = loadclass()

bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
print('bob:', bob.name, bob.acct, bob.age, bob.addr)

sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
print('sue:', sue.name, sue.acct, sue.age, sue.addr)  # addr은 다른 속성과 달리 클라이언트 데이터임
print('bob:', bob.name, bob.acct, bob.age, bob.addr)  # name, acct, age 값이 변경되는가?
