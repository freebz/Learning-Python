# 예외 발생시키기

try:
    raise IndexError            # 수동으로 예외 발생
except IndexError:
    print('got exception')

# got exception


raise IndexError
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError


assert False, 'Nobody expects the Spanish Inquisition'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError: Nobody expects the Spanish Inquisition
