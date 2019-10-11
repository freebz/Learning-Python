# 다른 인코딩 체계

S = 'A\u00c4B\U000000e8C'
S                               # A, B, C와 두 개의 아스크기 아닌 문자
# 'AÄBèC'
len(S)                          # 문자열 길이는 5
# 5

S.encode('latin-1')
# b'A\xc4B\xe8C'

len(S.encode('latin-1'))        # latin-1로 인코드되면 5바이트
# 5

S.encode('utf-8')
# b'A\xc3\x84B\xc3\xa8C'
len(S.encode('utf-8'))          # utf-8로 인코드되면 7바이트
# 7


S = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'
S
# 'AÄBèC'


S
# 'AÄBèC'
S.encode('cp500')               # 다른 서유럽 인코딩 두 가지
# b'\xc1c\xc2T\xc3'
S.encode('cp850')               # 5바이트의 서로 다른 인코드된 값
# b'A\x8eB\x8aC'

S = 'spam'                      # 대부분의 인코딩에서 아스키 텍스트는 동일함
S.encode('latin-1')
# b'spam'
S.encode('utf-8')
# b'spam'
S.encode('cp500')               # 하지만 cp500에서는 아스키도 다르게 표현됨. IBM EBCDIC!
# b'\xa2\x97\x81\x94'
S.encode('cp850')
# b'spam'


S = 'A\u00c4B\U000000e8C'
S.encode('utf-16')
# b'\xff\xfeA\x00\xc4\x00B\x00\xe8\x00C\x00'

S = 'spam'
S.encode('utf-16')
# b'\xff\xfes\x00p\x00a\x00m\x00'
S.encode('utf-32')
# b'\xff\xfe\x00\x00s\x00\x00\x00p\x00\x00\x00a\x00\x00\x00m\x00\x00\x00'
