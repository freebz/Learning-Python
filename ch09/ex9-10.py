# 패키징된 바이너리 데이터를 저장하기: struct

F = open('data.bin', 'wb')      # 바이너리 출력 파일 열기
import struct
data = struct.pack('>i4sh', 7, b'spam', 8) # 패키징된 바이너리 데이터 만들기
data
# b'\x00\x00\x00\x07spam\x00\x08'
F.write(data)
F.close()


F = open('data.bin', 'rb')
data = F.read()                 # 패키징된 바이너리 데이터 얻기
data
# b'\x00\x00\x00\x07spam\x00\x08'
values = struct.unpack('>i4sh', data) # 파이썬 객체로 변환
values
# (7, b'spam', 8)
