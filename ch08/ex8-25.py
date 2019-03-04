# has_key 메서드는 3.X에서 없어짐: 꽤 오래 생존했다!

D
# {'a': 1, 'b': 2, 'c': 3}

D.has_key('c')                  # 2.X에서만 동작: True/False 반환
# AttributeError: 'dict' object has no attribute 'has_key'

'c' in D                        # 3.X 필수
# True
'x' in D                        # 오늘날 2.X에서도 사용을 권장
# False
if 'c' in D: print('present', D['c']) # 결과를 통한 분기

# present 3

print(D.get('c'))               # 기본값 가져오기
# 3
print(D.get('x'))
# None
if D.get('c') != None: print('present', D['c']) # 다른 방법

# present 3
