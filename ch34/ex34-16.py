# raise를 이용한 예외 전달

try:
    raise IndexError('spam')    # 예외가 인수를 기억
except IndexError:
    print('propagating')
    raise                       # 가장 최근 발생한 예외를 다시 발생시킴

# propagating
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# IndexError: spam
