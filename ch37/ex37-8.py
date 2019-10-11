# 아스키가 아닌 텍스트 인코딩과 디코딩

S = '\u00c4\u00e8'              # 아스키가 아닌 텍스트 문자열: 두 글자 길이
S
# 'Äè'
len(S)
# 2

S.encode('ascii')
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)


S.encode('latin-1')             # 인코드된 글자는 글자당 1바이트
# b'\xc4\xe8'

S.encode('utf-8')               # 인코드된 글자는 글자당 2바이트
# b'\xc3\x84\xc3\xa8'

len(S.encode('latin-1'))        # latin-1에서는 2바이트, utf-8에서는 4바이트
# 2
len(S.encode('utf-8'))
# 4


B = b'\xc4\xe8'                 # Latin-1로 인코드된 텍스트
B
# b'\xc4\xe8'
len(B)                          # 2 raw 바이트, 인코드된 글자 두 개
# 2
B.decode('latin-1')             # Latin-1로 텍스트 디코드
# 'Äè'

B = b'\xc3\x84\xc3\xa8'         # UTF-8로 인코드도니 텍스트
len(B)                          # 4 raw 바이트, 인코드된 글자 두 개
# 4
B.decode('utf-8')               # UTF-8로 텍스트 디코드
# 'Äè'
len(B.decode('utf-8'))          # 메모리 안에는 두 개의 유니코드 문자가 존재
# 2
