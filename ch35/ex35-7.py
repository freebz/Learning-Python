# 사용자 정의 출력 디스플레이

class MyBad(Exception): pass

try:
    raise MyBad('Sorry--my mistake!')
except MyBad as X:
    print(X)

# Sorry--my mistake!


raise MyBad('Sorry--my mistake!')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.MyBad: Sorry--my mistake!


class MyBad(Exception):
    def __str__(self):
        return 'Always look on the bright side of life...'

try:
    raise MyBad()
except MyBad as X:
    print(X)

# Always look on the bright side of life...

raise MyBad()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.MyBad: Always look on the bright side of life...


class E(Exception):
    def __repr__(self): return 'Not called!'
raise E('spam')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.E: spam

class E(Exception):
    def __str__(self): return 'Called!'
raise E('spam')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.E: Called!
