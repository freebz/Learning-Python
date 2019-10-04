# 파일과 서버 연결 닫기

myfile = open(r'C:\code\textdata', 'w')
try:
    ...myfile 처리...
finally:
    myfile.close()


with open(r'C:\code\textdata', 'w') as myfile:
    ...myfile 처리...


myfile = open(filename, 'w')    # 전형적인 형태
...myfile 처리...
myfile.close()

with open(filename) as myfile:  # 콘텍스트 매니저 형태
    ...myfile 처리...
