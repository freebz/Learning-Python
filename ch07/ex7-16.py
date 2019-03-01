# 문자열 포매팅 표현식

# 포매팅 표현식의 기본

'That is %d %s bird!' % (1, 'dead') # 포매팅 표현식
# 'That is 1 dead bird!'


exclamation = 'Ni'
'The knights who say %s!' % exclamation # 문자열 대체
# 'The knights who say Ni!'

'%d %s %g you' % (1, 'spam', 4.0) # 타입별 대체
# '1 spam 4 you'

'%s -- %s -- %s' % (42, 3.14159, [1, 2, 3]) # %s 대상에는 모든 타입이 일치
# '42 -- 3.14159 -- [1, 2, 3]'
