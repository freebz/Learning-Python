# 예외: 백 투 더 퓨처

# 문자열 예외는 더 이상 사용하지 않는다!

# py -2
myexc = "My exception string"
try:
    raise myexc
except myexc:
    print('caught')

# caught


# py -3
raise 'spam'
# TypeError: exceptions must derive from BaseException

# py -2
raise 'spam'
# TypeError: exceptions must be old-style classes or derived from BaseException, not str
