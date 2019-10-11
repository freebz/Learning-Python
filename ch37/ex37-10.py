# 바이트 문자열 리터럴: 인코드된 텍스트

S = 'A\xC4B\xE8C'               # 3.X: str은 16진수와 유니코드 이스케이프를 모두 지원함
S
# 'AÄBèC'
S = 'A\u00C4B\U000000E8C'
S
# 'AÄBèC'

B = b'A\xC4B\xE8C'              # bytes은 16진수 이스케이프만 지원함
B
# b'A\xc4B\xe8C'
B = b'A\u00C4B\U000000E8C'      # 이스케이프 시퀀스가 문자 그대로 사용됨!
B
# b'A\\u00C4B\\U000000E8C'

B = b'A\xC4B\xE8C'              # bytes는 16진수 이스케이프 사용
B                               # 아스키가 아닌 문자를 16진수로 출력
# b'A\xc4B\xe8C'
print(B)
# b'A\xc4B\xe8C'
B.decode('latin-1')             # Latin-1로 디코드하여 텍스트로 출력
# 'AÄBèC'


S = 'AÄBèC'                     # 인코딩 선언이 없을 경우 UTF-8 문자로 인식
S
# 'AÄBèC'

B = b'AÄBèC'
# SyntaxError: bytes can only contain ASCII literal characters.

B = b'A\xC4B\xE8C'              # 문자는 아스키거나 이스케이프 문자여야 함
B
# b'A\xc4B\xe8C'
B.decode('latin-1')
# 'AÄBèC'

S.encode()                      # 소스 코드는 기본적으로 UTF-8로 인코드됨
# b'A\xc3\x84B\xc3\xa8C'        # 별도로 지정하지 않으면 시스템 기본 인코딩을 이용함
S.encode('utf-8')
# b'A\xc3\x84B\xc3\xa8C'

B.decode()                      # raw 바이트는 UTF-8에 대응되지 않음
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc4 in position 1: invalid continuation byte
