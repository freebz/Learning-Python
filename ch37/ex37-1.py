# 문자열 기초

# 문자 인코딩 방법

ord('a')                        # 'a'는 아스키 값 97을 가진 바이트
# 97
hex(97)
# '0x61'
chr(97)                         # 이진 값 97은 문자 'a'를 뜻함
# 'a'


0xC4
# 196
chr(196)                        # 파이썬 3.X 결과 형식
# 'Ä'


S = 'ni'
S.encode('ascii'), S.encode('latin1'), S.encode('utf8')
# (b'ni', b'ni', b'ni')

S.encode('utf16'), len(S.encode('utf16'))
# (b'\xff\xfen\x00i\x00', 6)

S.encode('utf32'), len(S.encode('utf32'))
# (b'\xff\xfe\x00\x00n\x00\x00\x00i\x00\x00\x00', 12)
