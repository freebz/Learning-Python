# 문자열 메서드 예제: 문자열 변환 II

S = 'spammy'
S = S[:3] + 'xx' + S[5:]        # S로부터 섹션 슬라이싱
S
# 'spaxxy'


S = 'spammy'
S = S.replace('mm', 'xx')       # S에서 모든 mm을 xx로 대체
S
# 'spaxxy'


'aa$bb$cc$dd'.replace('$', 'SPAM')
# 'aaSPAMbbSPAMccSPAMdd'


S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')          # 위치 검색
where
# 4
S = S[:where] + 'EGGS' + S[(where+4):]
S
# 'xxxxEGGSxxxxSPAMxxxx'


S = 'spammy'
L = list(S)
L
# ['s', 'p', 'a', 'm', 'm', 'y']


L[3] = 'x'                      # 리스트에서는 가능한 연산
L[4] = 'x'
L
# ['s', 'p', 'a', 'x', 'x', 'y']


S = ''.join(L)
S
# 'spaxxy'


'SPAM'.join(['eggs', 'sausage', 'ham', 'toast'])
# 'eggsSPAMsausageSPAMhamSPAMtoast'
