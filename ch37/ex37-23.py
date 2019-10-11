# 3.X에서 타입과 내용 불일치

# 파일 내용의 타입은 유연하지 않음
open('temp', 'w').write('abc\n')      # 텍스트 모드는 str로 입출력함
# 4
open('temp', 'w').write(b'abc\n')
# TypeError: write() argument must be str, not bytes

open('temp', 'wb').write(b'abc\n')    # 바이너리 모드는 bytes로 입출력해야 함
# 4
open('temp', 'wb').write('abc\n')
# TypeError: a bytes-like object is required, not 'str'


# 진정한 바이너리 데이터는 텍스트 모드에서 읽을 수 없음
chr(0xFF)                                    # FF는 유요한 문자, FE는 유효하지 않음
# 'ÿ'
chr(0xFE)                                    # 일부 파이썬 버전에서는 오류 발생
# 'þ'

open('temp', 'w').write(b'\xFF\xFE\xFD')     # 임의의 bytes 사용 불가!
# TypeError: write() argument must be str, not bytes

open('temp', 'w').write('\xFF\xFE\xFD')      # str 내에 포함되었을 경우 사용 가능
# 3
open('temp', 'wb').write(b'\xFF\xFE\xFD')    # 바이너리 모드로도 쓸 수 있음
# 3

open('temp', 'rb').read()                    # 바이너리 bytes로 읽기 가능
# b'\xff\xfe\xfd'

open('temp', 'r').read()                     # 디코드 가능한 텍스트가 아니면 읽을 수 없음!
# 'ÿ\xfe\xfd'                                # 일부 파이썬 버전에서는 오류 발생
