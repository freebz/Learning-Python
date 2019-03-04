# 리스트 정렬에 대한 자세한 이야기

L = ['abc', 'ABD', 'aBe']
L.sort()                        # 대소문자 혼합된 리스트 정렬
L
# ['ABD', 'aBe', 'abc']
L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower)           # 소문자 비교
L
# ['abc', 'ABD', 'aBe']

L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True) # 정렬 순서 변경
L
# ['aBe', 'ABD', 'abc']


L = ['abc', 'ABD', 'aBe']
sorted(L, key=str.lower, reverse=True) # 내장 함수로 정렬
# ['aBe', 'ABD', 'abc']

L = ['abc', 'ABD', 'aBe']
sorted([x.lower() for x in L], reverse=True) # 미리 변환: 결과가 다르다!
# ['abe', 'abd', 'abc']
