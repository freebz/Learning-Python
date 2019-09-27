# 어째서 예외를 사용해야 하는가?

# 예외: 짧은 이야기

# 기본 예외 처리기

def fetcher(obj, index):
    return obj[index]


x = 'spam'
fetcher(x, 3)                   # x[3]과 유사함
# 'm'


fetcher(x, 4)                   # 기본 예외 처리기 -- 쉘 인터페이스
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in fetcher
#     return obj[index]
# IndexError: string index out of range


fetcher(x, 4)                   # 기본 예외 처리기 -- IDLE GUI 인터페이스
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     fetcher(x, 4)
#   File "<pyshell#3>", line 2, in fetcher
#     return obj[index]
# IndexError: string index out of range
