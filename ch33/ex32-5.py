# 종료 동작

try:
    fetcher(x, 3)
finally:                        # 종료 동작
    print('after fetch')

# 'm'
# after fetch


fetcher(x, 3)
print('after fetch')


def after():
    try:
        fetcher(x, 4)
    finally:
        print('after fetch')
    print('after try?')

after()
# after fetch
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 3, in after
#   File "<stdin>", line 2, in fetcher
# IndexError: string index out of range


def after():
    try:
        fetcher(x, 3)
    finally:
        print('after fetch')
    print('after try?')

after()
# after fetch
# after try?


with open('lumberjack.txt', 'w') as file:    # 종료 시 언제나 파일을 닫음
    file.write('The larch!\n')
