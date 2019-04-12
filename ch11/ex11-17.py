# 수동 스트림 리다이렉션

print(X, Y)                     # 또는 2.X에서 print X, Y


import sys
sys.stdout.write(str(X) + ' ' + str(Y) + '\n')


import sys
sys.stdout = open('log.txt', 'a') # 파일로 출력을 리다이렉트
...
print(x, y, x)                  # log.txt에 표시됨
