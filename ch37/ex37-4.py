# 파이썬 2.X 문자열 리터럴

# py -2
B = b'spam'                     # 3.X의 바이트 리터럴은 2.6/2.7에서는 단순 str임
S = 'eggs'                      # str은 바이트/문자 시퀀스임

type(B), type(S)
# (<type 'str'>, <type 'str'>)
B, S
# ('spam', 'eggs')
list(B), list(S)
# (['s', 'p', 'a', 'm'], ['e', 'g', 'g', 's'])


U = u'spam'                     # 2.X 유니코드 리터럴은 별도의 타입을 생성함
type(U)                         # 3.6에서도 동작하지만, 단순 str임
# <type 'unicode'>
U
# u'spam'
U[0]
# u's'
list(U)
# [u's', u'p', u'a', u'm']
