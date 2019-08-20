# 셸브를 대화형으로 알아보기

import glob
glob.glob('person*')
# ['persondb', 'person-department.py', 'person.py', 'person-composite.py']

print(open('persondb.dir').read())
# 'Sue Jones', (512, 92)
# 'Tom Jones' (1024, 91)
# 'Bob Smith' (0, 80)

print(open('persondb.dat','rb').read())
# b'\x80\x03cperson\nPerson\nq\x00\)\x81q\x01}q\x02(X\x03\x00\x00\x00jobq\x03NX\x03\x00
# ...이후 생략...


import shelve
db = shelve.open('persondb')                 # 셸브를 다시 염

len(db)                                      # 세 개의 '레코드들'이 저장됨
# 3
list(db.keys())                              # keys는 인덱스
# ['Tom Jones', 'Sue Jones', 'Bob Smith']    # list()는 3.X에서 리스트로 만들어줌

bob = db['Bob Smith']                        # 키로 bob 가져오기
bob                                          # AttrDisplay로부터 __repr__ 실행
# [Person: Bob Smith, 0]

bob.lastName()                               # Person으로부터 lastName 실행
# 'Smith'

for key in db:                               # 반복, 가져오기, 출력하기
    print(key, '=>', db[key])

# Tom Jones => [Person: Tom Jones, 50000]
# Sue Jones => [Person: Sue Jones, 100000]
# Bob Smith => [Person: Bob Smith, 0]

for key in sorted(db):
    print(key, '=>', db[key])                # 정렬된 키로 반복하기

# Bob Smith => [Person: Bob Smith, 0]
# Sue Jones => [Person: Sue Jones, 100000]
# Tom Jones => [Person: Tom Jones, 50000]
