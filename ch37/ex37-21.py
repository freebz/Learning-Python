# 텍스트 파일과 바이너리 파일 사용하기

# 텍스트 파일 기초

# py -3
# 기본적인 텍스트 파일과 문자열은 2.X와 동일하게 동작함

file = open('temp', 'w')
size = file.write('abc\n')      # 기록된 문자 수를 반환
file.close()                    # 출력 버퍼를 비우기 위해 수동으로 close

file = open('temp')             # 기본 모드는 "r" (== "rt"): 텍스트 입력
text = file.read()
text
# 'abc\n'
print(text)
# abc
#
