# 파이썬 3.X 키워드 전용 인수

def kwonly(a, *b, c):
    print(a, b, c)

kwonly(1, 2, c=3)
# 1 (2,) 3
kwonly(a=1, c=3)
# 1 () 3
kwonly(1, 2, 3)
# TypeError: kwonly() missing 1 required keyword-only argument: 'c'


def kwonly(a, *, b, c):
    print(a, b, c)

kwonly(1, c=3, b=2)
# 1 2 3
kwonly(c=3, b=2, a=1)
# 1 2 3
kwonly(1, 2, 3)
# TypeError: kwonly() takes 1 positional argument but 3 were given
kwonly(1)
# TypeError: kwonly() missing 2 required keyword-only arguments: 'b' and 'c'


def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)

kwonly(1)
# 1 spam ham
kwonly(1, c=3)
# 1 spam 3
kwonly(a=1)
# 1 spam ham
kwonly(c=3, b=2, a=1)
# 1 2 3
kwonly(1, 2)
# TypeError: kwonly() takes 1 positional argument but 2 were given


def kwonly(a, *, b, c='spam'):
    print(a, b, c)

kwonly(1, b='eggs')
# 1 eggs spam
kwonly(1, c='eggs')
# TypeError: kwonly() missing 1 required keyword-only argument: 'b'
kwonly(1, 2)
# TypeError: kwonly() takes 1 positional argument but 2 were given

def kwonly(a, *, b=1, c, d=2):
    print(a, b, c, d)

kwonly(3, c=4)
# 3 1 4 2
kwonly(3, c=4, b=5)
# 3 5 4 2
kwonly(3)
# TypeError: kwonly() missing 1 required keyword-only argument: 'c'
kwonly(1, 2, 3)
# TypeError: kwonly() takes 1 positional argument but 3 were given
