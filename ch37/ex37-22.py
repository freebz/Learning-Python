# 2.X와 3.X에서 텍스트와 바이너리 모드

# py -2
open('temp', 'w').write('abd\n')      # 텍스트 모드 쓰기: \r추가
open('temp', 'r').read()              # 텍스트 모드 읽기: \r제거
# 'abd\n'
open('temp', 'rb').read()             # 바이너리 모드 읽기: 그대로 읽음
# 'abd\r\n'

open('temp', 'wb').write('abc\n')     # 바이너리 모드 쓰기
open('temp', 'r').read()              # \n이 \r\n으로 확장되지 않음
# 'abd\n'
open('temp', 'rb').read()
# 'abd\n'


# py -3
# 텍스트 파일에 쓰고 읽음
open('temp', 'w').write('abc\n')       # 텍스트 모드 쓰기: str 제공
# 4
open('temp', 'r').read()               # 텍스트 모드 읽기: str 반환
# 'abc\n'
open('temp', 'rb').read()              # 바이너리 모드 읽기: bytes 반환
# b'abc\r\n'


# 바이너리 파일에 쓰고 읽음
open('temp', 'wb').write(b'abc\n')     # 바이너리 모드 쓰기. bytes 사용
# 4
open('temp', 'r').read()               # 텍스트 모드 읽기. str 반환
# 'abc\n'
open('temp', 'rb').read()              # 바이너리 모드 읽기. bytes 반환
# b'abc\n'


# 실제 바이너리 데이터를 쓰고 읽음
open('temp', 'wb').write(b'a\x00c')    # bytes 쓰기
# 3
open('temp', 'r').read()               # str 반환
# 'a\x00c'
open('temp', 'rb').read()              # bytes 반환
# b'a\x00c'


# bytearray도 동작함
BA = bytearray(b'\x01\x02\x03')

open('temp', 'wb').write(BA)
# 3
open('temp', 'r').read()
# '\x01\x02\x03'
open('temp', 'rb').read()
# b'\x01\x02\x03'
