# 인코딩 변환하기

B = b'A\xc3\x84B\xc3\xa8C'      # 원래 UTF-8 포맷으로 인코드된 텍스트
S = B.decode('utf-8')           # UTF-8로 유니코드 텍스트로 디코드함
S
# 'AÄBèC'

T = S.encode('cp500')           # EBCDIC로 인코드된 bytes로 변환함
T
# b'\xc1c\xc2T\xc3'

U = T.decode('cp500')           # EBCDIC로 다시 유니코드로 변환함
U
# 'AÄBèC'

U.encode()                      # 다시 기본값인 utf-8로 인코드함
# b'A\xc3\x84B\xc3\xa8C'
