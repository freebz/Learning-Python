# 바이너리 바이트 파일

import struct
packed = struct.pack('>i4sh', 7, b'spam', 8)    # 패키지된 바이너리 데이터
packed                                          # 10바이트, 객체가 아닌 텍스트
# b'\x00\x00\x00\x07spam\x00\x08'

file = open('data.bin', 'wb')                   # 바이너리 출력 파일 열기
file.write(packed)                              # 패키지된 바이너리 데이터 쓰기
# 10
file.close()


data = open('data.bin', 'rb').read()            # 바이너리 데이터 파일을 열고 읽음
data                                            # 변경되지 않은 10바이트
# b'\x00\x00\x00\x07spam\x00\x08'
data[4:8]                                       # 중간 데이터를 잘라냄
# b'spam'
list(data)                                      # 8비트 바이트의 연속
# [0, 0, 0, 7, 115, 112, 97, 109, 0, 8]
struct.unpack('>i4sh', data)                    # 다시 객체로 품(unpack)
# (7, b'spam', 8)
