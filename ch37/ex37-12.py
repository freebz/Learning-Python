# 파이썬 2.X에서 유니코드 문자열 코딩하기

# py -2
S = 'A\xC4B\xE8C'               # 8비트 바이트 문자열
S                               # Latin-1로 인코드된 텍스트(일부는 아스키가 아닌 문자임)
# 'A\xc4B\xe8C'
print S                         # 출력 불가능한 문자(IDLE은 다를 수 있음)
# A�B�C


U = S.decode('latin-1')         # Latin-1에 의해 bytes를 유니코드 텍스트로 디코드함
U
# u'A\xc4B\xe8C'
print U
# AÄBèC

S.decode('utf-8')               # 인코드된 형태가 utf-8과 호환되지 않음
# UnicodeDecodeError: 'utf8' codec can't decode byte 0xc4 in position 1: invalid continuation byte

S.decode('ascii')               # 인코드된 bytes도 아스키 범위를 벗어남
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 1: ordinal not in range(128)


U = u'A\xC4B\xE8C'              # 유니코드 문자열 생성, 16진수 이스케이프
U
# u'A\xc4B\xe8C'
print U
# AÄBèC


U.encode('latin-1')             # Latin-1에 의해 인코드한 8비트 bytes
# 'A\xc4B\xe8C'

U.encode('utf-8')               # utf-8에 의해 인코드한 멀티바이트
# 'A\xc3\x84B\xc3\xa8C'


# py -2
U = u'A\xC4B\xE8C'              # 아스키가 아닌 문자에 대한 16진수 이스케이프
U
# u'A\xc4B\xe8C'
print U
# AÄBèC

U = u'A\u00C4B\U000000E8C'      # 아스키 문자에 대한 유니코드 이스케이프
U
# u'A\xc4B\xe8C'
print U
# AÄBèC

S = 'A\xC4B\xE8C'               # 16진수 이스케이프도 동작함
S
# 'A\xc4B\xe8C'
print S                         # 디코드하지 않은 일부 문자는 이상하게 출력됨
# A�B�C
print S.decode('latin-1')
# AÄBèC

S = 'A\u00C4B\U000000E8C'       # 유니코드 이스케이프 아님. 리터럴로 해석!
S
# 'A\\u00C4B\\U000000E8C'
print S
# A\u00C4B\U000000E8C
len(S)
# 19
