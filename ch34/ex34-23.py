# 다중 콘텍스트 관리자(파이썬 3.1, 2.7 그리고 그 이후 버전)

with open('data') as fin, open('res', 'w') as fout:
    for line in fin:
        if 'some key' in line:
            fout.write(line)


with A() as a, B() as b:
    ...구문...


with A() as a:
    with B() as b:
        ...구문...


with open('script1.py') as f1, open('script2.py') as f2:
    for pair in zip(f1, f2):
        print(pair)
        
# ('# A first Python script\n', 'import sys\n')
# ('import sys                  # Load a library module\n', 'print(sys.path)\n')
# ('print(sys.platform)\n', 'x = 2\n')
# ('print(2 ** 32)              # Raise 2 to a power\n', 'print(x**32)\n')


with open('script1.py') as f1, open('script2.py') as f2:
    for (linenum, (line1, line2)) in enumerate(zip(f1, f2)):
        if line1 != line2:
            print('%s\n%r\n%r' % (linenum, line1, line2))


for pair in zip(open('script1.py'), open('script2.py')): # 동일한 효과(자동 닫음)
    print(pair)


with open('script2.py') as fin, open('upper.py', 'w') as fout:
    for line in fin:
        fout.write(line.upper())

print(open('upper.py').read())
# IMPORT SYS
# PRINT(SYS.PATH)
# X = 2
# PRINT(X**32)


fin  = open('script2.py')
fout = open('upper.py', 'w')
for line in fin:            # 이전 코드와 같은 효과를 내며, 자동으로 파일을 닫음
    fout.write(line.upper())


fin  = open('script2.py')
fout = open('upper.py', 'w')
try:                        # 같은 효과를 내지만, 오류 발생 시 명시적으로 파일을 닫음
    for line in fin:
        fout.write(line.upper())
finally:
    fin.close()
    fout.close()
