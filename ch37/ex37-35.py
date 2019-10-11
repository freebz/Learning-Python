# struct 바이너리 데이터 모듈

# py -3
from struct import pack
pack('>i4sh', 7, b'spam', 8)    # 3.X에서는 bytes 타입(8비트 문자열)
# b'\x00\x00\x00\x07spam\x00\x08'


# py -2
from struct import pack
pack('>i4sh', 7, 'spam', 8)     # 2.X에서는 문자열 타입(8비트 문자열)
# '\x00\x00\x00\x07spam\x00\x08'


# py -3
import struct
B = struct.pack('>i4sh', 7, b'spam', 8)
B
# b'\x00\x00\x00\x07spam\x00\x08'

vals = struct.unpack('>i4sh', B)
vals
# (7, b'spam', 8)

vals = struct.unpack('>i4sh', B.decode())
# TypeError: a bytes-like object is required, not 'str'


# py -3
# 패킹된 바이너리 파일에 값 기록
F = open('data.bin', 'wb')                    # 바이너리 결과 파일 열기
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)    # 패킹된 바이너리 데이터 생성
data
# b'\x00\x00\x00\x07spam\x00\x08'
F.write(data)                                 # 파일에 기록
# 10
F.close()

# 패킹된 바이너리 파일에서 값을 읽음
F = open('data.bin', 'rb')                    # 바이너리 입력 파일 열기
data = F.read()                               # 바이트 읽기
data
# b'\x00\x00\x00\x07spam\x00\x08'
values = struct.unpack('>i4sh', data)         # 패킹된 바이너리 데이터 추출
values
# (7, b'spam', 8)


values                          # struct.unpack의 결과
# (7, b'spam', 8)

# 파싱한 정수의 비트에 접근함
bin(values[0])                  # 정수의 비트에 접근 가능함
# '0b111'
values[0] & 0x01                # 정수의 첫 비트가 세팅되었는지 확인함
# 1
values[0] | 0b1010              # 비트 or 연산: 비트 값을 세팅함
# 15
bin(values[0] | 0b1010)         # 10진수 15는 2진수 1111
# '0b1111'
bin(values[0] ^ 0b1010)         # 비트 xor 연산: 모두 참일 경우 비트 값을 세팅하지 않음
# '0b1101'
bool(values[0] & 0b100)         # 세 번째 비트가 세팅되었는지 확인
# True
bool(values[0] & 0b1000)        # 네 번째 비트가 세팅되었는지 확인
# False


# 파싱된 문자열의 바이트와 그 바이트 내의 비트에 접근함
values[1]
# b'spam'
values[1][0]                    # bytes 문자열: 정수 시퀀스
# 115
values[1][1:]                   # 아스키 문자로 출력됨
# b'pam'
bin(values[1][0])               # 문자열의 바이트 비트에 접근할 수 있음
# '0b1110011'
bin(values[1][0] | 0b1100)      # 비트를 변경
# '0b1111111'
values[1][0] | 0b1100
# 127
