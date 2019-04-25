# 반복 프로토콜: 파일 반복자(Iterator)

print(open('script2.py').read())
# import sys
# print(sys.path)
# x = 2
# print(x ** 32)

open('script2.py').read()
# 'import sys\nprint(sys.path)\nx = 2\nprint(x ** 32)\n'


f = open('script2.py')          # 현재 디렉터리에서 네 라인으로 된 스크립트 파일 읽기
f.readline()                    # readline은 호출될 때마다 한 라인을 읽음
# 'import sys\n'
f.readline()
# 'print(sys.path)\n'
f.readline()
# 'x = 2\n'
f.readline()                    # 마지막 라인에는 \n이 없을 수도 있음
# 'print(x ** 32)\n'
f.readline()                    # 파일의 끝에서 빈 문자열을 반한함
# ''


f = open('script2.py')          # __next__ 또한 호출될 때마다 한 라인을 읽음
f.__next__()                    # 그러나 파일의 끝에서 예외를 발생시킴
# 'import sys\n'
f.__next__()                    # 2.X에서는 f.next()를 사용하거나 2.X 또는 3.X에서 next(f)를 사용하자
# 'print(sys.path)\n'
f.__next__()
# 'x = 2\n'
f.__next__()
# 'print(x ** 32)\n'
f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration


for line in open('script2.py'): # 라인 단위로 읽기 위해 파일 반복자 사용
    print(line.upper(), end='') # __next__ 호출. StopIteration 예외 처리

# IMPORT SYS
# PRINT(SYS.PATH)
# X = 2
# PRINT(X ** 32)


for line in open('script2.py').readlines():
    print(line.upper(), end='')

# IMPORT SYS
# PRINT(SYS.PATH)
# X = 2
# PRINT(X ** 32)


f = open('script2.py')
while True:
    line = f.readline()
    if not line: break
    print(line.upper(), end='')

# ...동일한 출력...
