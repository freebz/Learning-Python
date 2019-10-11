# 파이썬 3.6에서 파이썬 2.X의 유니코드 리터럴 사용

# py -3
U = u'spam'                     # 2.X의 유니코드 리터럴은 3.3 이후에서 도임됨
type(U)                         # str이지만 하위 호환됨
# <class 'str'>
U
# 'spam'
U[0]
# 's'
list(U)
# ['s', 'p', 'a', 'm']
