# 딕셔너리를 만드는 다른 방법

{'name': 'Bob', 'age': 40 }     # 전통적인 리터럴 표현식

D = {}                          # 동적으로 키 할당하기
D['name'] = 'Bob'
D['age'] = 40

dict(name='Bob', age=40)        # dict 키워드 인수 형식

dict([('name', 'Bob'), ('age', 40)]) # dict 키/값 튜플 형식


dict(zip(keyslist, valueslist)) # 딕셔너리에 키/값 튜플 형식을 묶기(zip)


dict.fromkeys(['a', 'b'], 0)
# {'a': 0, 'b': 0}
