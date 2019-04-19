# 더 생각해 볼 주제: 파일 스캐너

file = open('test.txt', 'r')    # 파일 콘텐츠를 문자열로 읽기
print(file.read())


file = open('test.txt')
while True:
    char = file.read(1)         # 문자 단위로 읽기
    if not char: break          # 빈 문자열은 파일의 끝을 의미
    print(char)

for char in open('test.txt').read():
    print(char)


file = open('test.txt')
while True:
    line = file.readline()      # 라인 단위로 읽기
    if not line: break
    print(line.rstrip())        # 라인 안에 이미 \n이 포함

file = open('test.txt', 'rb')
while True:
    chunk = file.read(10)       # 바이트 덩어리 읽기: 10바이트까지
    if not chunk: break
    print(chunk)


for line in open('test.txt').readlines():
    print(line.rstrip())

for line in open('test.txt'):   # 반복자 사용: 텍스트 입력 처리에 최적
    print(line.rstrip())


for line in reversed(open('test.txt').readlines()): ...
