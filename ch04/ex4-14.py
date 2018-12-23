# 딕셔너리

# 매핑 연산

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}


D['food']                       # 키 'food'에 대한 값 가져오기
# 'Spam'

D['quantity'] += 1              # 'quantity'의 값에 1 더하기
D
# {'food': 'Spam', 'quantity': 5, 'color': 'pink'}


D = {}
D['name'] = 'Bob'               # 할당에 의해 새로운 키 생성
D['job'] = 'dev'
D['age'] = 40

D
# {'name': 'Bob', 'job': 'dev', 'age': 40}

print(D['name'])
# Bob


bob1 = dict(name='Bob', job='dev', age=40) # 키워드
bob1
# {'name': 'Bob', 'job': 'dev', 'age': 40}

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])) # 압축
bob2
# {'name': 'Bob', 'job': 'dev', 'age': 40}
