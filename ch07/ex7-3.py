# 원시(raw) 문자열은 이스케이프의 동작을 막음

myfile = open('C:\new\text.dat', 'w')


myfile = open(r'C:\new\text.dat', 'w')


myfile = open('C:\\new\\text.dat', 'w')


path = r'C:\new\text.dat'
path                            # 파이썬 코드처럼 출력
# 'C:\\new\\text.dat'
print(path)                     # 사용자 친화적인 형식
# C:\new\text.dat
len(path)                       # 문자열 길이
# 15
