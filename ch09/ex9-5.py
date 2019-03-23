# 파일

# 파일의 동작

myfile = open('myfile.txt', 'w') # 텍스트 출력을 위해 열기: 빈 파일 생성
myfile.write('hello text file\n') # 한 라인의 텍스트 쓰기: 문자열
# 16
myfile.write('goodbye text file\n')
# 18
myfile.close()                  # 출력 버퍼를 디스크로 비우기

myfile = open('myfile.txt')     # 텍스트 입력을 위해 열기: 'r'은 기본값
myfile.readline()               # 라인을 다시 읽기
# 'hello text file\n'
myfile.readline()
# 'goodbye text file\n'
myfile.readline()               # 빈 문자열: 파일의 끝
# ''


open('myfile.txt').read()       # 한 번에 모든 내용을 문자열로 읽기
# 'hello text file\ngoodbye text file\n'

print(open('myfile.txt').read()) # 좀 더 익숙한 출력 방식
# hello text file
# goodbye text file


for line in open('myfile.txt'): # 읽지 않고 파일 반복자 사용
    print(line, end='')

# hello text file
# goodbye text file
