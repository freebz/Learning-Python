# 기본 출력 기능과 상태 정보 유지 기능

raise IndexError                # IndexError()와 동일: 인수가 없음
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError

raise IndexError('spam')        # 생성자 인수가 첨부되고 출력됨
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: spam

I = IndexError('sapm')          # 객체 속성에 존재함
I.args
# ('sapm',)
print(I)                        # 수동으로 출력될 때 args가 표시됨
# sapm


class E(Exception): pass

raise E
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.E

raise E('spam')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.E: spam

I = E('spam')
I.args
# ('spam',)
print(I)
# spam


try:
    raise E('spam')
except E as X:
    print(X)                    # 생성자 인수들을 표시하고 저장함
    print(X.args)
    print(repr(X))

# spam
# ('spam',)
# E('spam',)
try:                            # 다중 인수들은 튜플로 저장되고 표시됨
    raise E('spam', 'eggs', 'ham')
except E as X:
    print('%s %s' % (X, X.args))

# ('spam', 'eggs', 'ham') ('spam', 'eggs', 'ham')
