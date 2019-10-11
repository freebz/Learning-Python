# 수동 인코딩

# 메서드로 수동 인코드
L = S.encode('latin-1')         # latin-1로 인코드 시 5바이트
L
# b'A\xc4B\xe8C'
len(L)
# 5

U = S.encode('utf-8')           # utf-8로 인코드 시 7바이트
U
# b'A\xc3\x84B\xc3\xa8C'
len(U)
# 7
