# 파이썬 객체를 파일에 저장하기: 변환

X, Y, Z = 43, 44, 45            # 네이티브 파이썬 객체들
S = 'Spam'                      # 파일에 저장하기 위해서 문자열이어야 함
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')   # 출력 텍스트 파일 만들기
F.write(S + '\n')               # \n으로 라인 종료
F.write('%s,%s,%s\n' % (X, Y, Z)) # 숫자를 문자열로 변환
F.write(str(L) + '$' + str(D) + '\n') # 변환하고 $로 구분
F.close()


chars = open('datafile.txt').read() # 원시 문자열 출력
chars
# "Spam\n43,44,45\n[1, 2, 3]${'a': 1, 'b': 2}\n"
print(chars)                    # 사용자에게 익숙한 형태로 출력
# Spam
# 43,44,45
# [1, 2, 3]${'a': 1, 'b': 2}


F = open('datafile.txt')        # 다시 열기
line = F.readline()             # 한 라인 읽기
line
# 'Spam\n'
line.rstrip()                   # 라인 끝 제거
# 'Spam'


line = F.readline()             # 파일에서 다음 라인 읽기
line                            # 여기서는 문자열
# '43,44,45\n'
parts = line.split(',')         # 콤마로 구분하기
parts
# ['43', '44', '45\n']


int(parts[1])                   # 문자열을 정수로 변환
# 44
numbers = [int(P) for P in parts] # 리스트의 내용을 한 번에 변환
numbers
# [43, 44, 45]


line = F.readline()
line
# "[1, 2, 3]${'a': 1, 'b': 2}\n"
parts = line.split('$')         # $로 분할
parts
# ['[1, 2, 3]', "{'a': 1, 'b': 2}\n"]
eval(parts[0])                  # 특정 객체 타입으로 변환
# [1, 2, 3]
objects = [eval(P) for P in parts] # 리스트 안의 모든 항목을 변환
objects
# [[1, 2, 3], {'a': 1, 'b': 2}]
