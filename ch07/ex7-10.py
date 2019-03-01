# 문자열 변환 I

S = 'spam'
S[0] = 'x'                      # 에러 발생
# TypeError: 'str' object does not support item assignment


S = S + 'SPAM!'                 # 문자열을 변경하기 위해 새로운 문자열 생성
S
# 'spamSPAM!'
S = S[:4] + 'Burger' + S[-1]
S
# 'spamBurger!'


S = 'splot'
S = S.replace('pl', 'pamal')
S
# 'spamalot'


'That is %d %s bird!' % (1, 'dead') # 포매팅 표현식: 모든 파이썬에서 지원
# 'That is 1 dead bird!'
'That is {0} {1} bird!'.format(1, 'dead') # 2.6, 2.7, 3.X에서 지원하는 포매팅 메서드
# 'That is 1 dead bird!'
