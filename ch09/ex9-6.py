# 텍스트 파일과 바이너리 파일에 대한 짧은 이야기

data = open('data.bin', 'rb').read() # 바이너리 파일 열기: rb = read binary
data                                 # bytes 문자열은 바이너리 데이터를 보관
# b'\x00\x00\x00\x07spam\x00\x08'
data[4:8]                            # 문자열처럼 동작
# b'spam'
data[4:8][0]                         # 그러나 실제는 작은 8비트 정수
# 115
bin(data[4:8][0])                    # 파이썬 3.X/2.6+ bin() 함수
'0b1110011'
