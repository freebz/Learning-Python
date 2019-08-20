# 셸브에서 객체 업데이트하기

# updatedb.py 파일: 데이터베이스의 Person 객체를 업데이트

import shelve
db = shelve.open('persondb')    # 동일한 파일명으로 셸브를 다시 염

for key in sorted(db):          # 데이터베이스 객체들을 보여 주기 위해 반복
    print(key, '\t=>', db[key]) # 커스터마이즈 포맷으로 출력

sue = db['Sue Jones']           # 가져오기 위해 키에 의해 인덱싱
sue.giveRaise(.10)              # 클래스의 메서드를 사용하여 메모리를 업데이트함
db['Sue Jones'] = sue           # 셸브에 업데이트하기 위해 키에 할당함
db.close()                      # 변경 후 데이터베이스를 닫음


# python updatedb.py
# Bob Smith 	=> [Person: job=None, name=Bob Smith, pay=0]
# Sue Jones 	=> [Person: job=dev, name=Sue Jones, pay=100000]
# Tom Jones 	=> [Manager: job=mgr, name=Tom Jones, pay=50000]

# python updatedb.py
# Bob Smith 	=> [Person: job=None, name=Bob Smith, pay=0]
# Sue Jones 	=> [Person: job=dev, name=Sue Jones, pay=110000]
# Tom Jones 	=> [Manager: job=mgr, name=Tom Jones, pay=50000]

# python updatedb.py
# Bob Smith 	=> [Person: job=None, name=Bob Smith, pay=0]
# Sue Jones 	=> [Person: job=dev, name=Sue Jones, pay=121000]
# Tom Jones 	=> [Manager: job=mgr, name=Tom Jones, pay=50000]

# python updatedb.py
# Bob Smith 	=> [Person: job=None, name=Bob Smith, pay=0]
# Sue Jones 	=> [Person: job=dev, name=Sue Jones, pay=133100]
# Tom Jones 	=> [Manager: job=mgr, name=Tom Jones, pay=50000]


# python
import shelve
db = shelve.open('persondb')    # 데이터베이스를 다시 염
rec = db['Sue Jones']           # 객체를 키에 의해 가져옴
rec
# [Person: Sue Jones, 146410]
rec.lastName()
# 'Jones'
rec.pay
# 146410
