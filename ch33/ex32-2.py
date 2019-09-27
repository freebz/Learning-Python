# 예외 처리하기

try:
    fetcher(x, 4)
except IndexError:              # 예외를 잡아내고 복구
    print('got exception')

# got exception


def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print('got exception')
    print('continuing')

catcher()
# got exception
# continuing
