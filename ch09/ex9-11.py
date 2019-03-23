# 파일 콘텍스트 매니저

with open(r'C:\code\data.txt') as myfile: # 자세한 내용은 34장 참조
    for line in myfile:
        ...여기서 읽은 라인을 사용...



myfile = open(r'C:\code\data.txt')
try:
    for line in myfile:
        ...여기서 읽은 라인을 사용...
finally:
    myfile.close()
