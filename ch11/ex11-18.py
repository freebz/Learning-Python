# 자동 스트림 리다이렉션

# c:\python36\python
import sys
temp = sys.stdout                    # 나중에 복구를 위해 저장
sys.stdout = open('log.txt', 'a')    # 출력을 파일로 리다이렉트
print('spam')                        # 파일로 출력
print(1, 2, 3)
sys.stdout.close()                   # 디스크로 출력을 flush
sys.stdout = temp                    # 원래 스트림 복구

print('back here')                   # 다시 화면으로 출력
# back here
print(open('log.txt').read())        # 이전 출력 결과
# spam
# 1 2 3


log = open('log.txt', 'a')      # 3.X
print(x, y, z, file=log)        # 파일과 유샇나 객체에 출력
print(a, b, c)                  # 기존 stdout으로 출력

log = open('log.txt', 'a')      # 2.X
print >> log, x, y, z           # 파일과 유사한 객체에 출력
print a, b, c                   # 기존 stdout으로 출력


# c:\python36\python
log = open('log.txt', 'w')
print(1, 2, 3, file=log)        # 2.X의 경우: print >> log, 1, 2, 3
print(4, 5, 6, file=log)
log.close()
print(7, 8, 9)                  # 2.X의 경우: print 7, 8, 9
# 7 8 9
print(open('log.txt').read())
# 1 2 3
# 4 5 6


import sys
sys.stderr.write(('Bad!' * 8) + '\n')
# Bad!Bad!Bad!Bad!Bad!Bad!Bad!Bad!

print('Bad!' * 8, file=sys.stderr)    # 2.X에서: print >> sys.stderr,'Bad!' * 8
# Bad!Bad!Bad!Bad!Bad!Bad!Bad!Bad!


X = 1; Y = 2
print(X, Y)                     # 출력 쉬운 방법
# 1 2
import sys                      # 출력: 어려운 방법
sys.stderr.write(str(X) + ' ' + str(Y) + '\n')
# 1 2
# 4


print(X, Y, file=open('temp1', 'w'))                   # 텍스트를 파일로 리다이렉트

open('temp2', 'w').write(str(X) + ' ' + str(Y) + '\n') # 수동으로 파일로 보내기
# 4
print(open('temp1', 'rb').read())                      # 바이너리 모드
# b'1 2\n'
print(open('temp2', 'rb').read())
# b'1 2\n'
