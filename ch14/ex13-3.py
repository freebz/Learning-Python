# 수동 반복: iter와 next

f = open('script2.py')
f.__next__()                    # 반복 메서드 직접 호출
# 'import sys\n'
f.__next__()
# 'print(sys.path)\n'

f = open('script2.py')
next(f)                         # 3.X에서 내장 next(f)는 f.__next__()를 호출
# 'import sys\n'
next(f)                         # next(f) => [#.X:f.__next__(), [2.X:f.next()]
# 'print(sys.path)\n'
