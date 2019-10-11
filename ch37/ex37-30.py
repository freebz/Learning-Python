# 파이썬에서 BOM 제거하기

open('temp.txt', 'w', encoding='utf-8').write('spam\nSPAM\n')
# 10
open('temp.txt', 'rb').read()       # BOM 없음
# b'spam\nSPAM\n'

open('temp.txt', 'w', encoding='utf-8-sig').write('spam\nSPAM\n')
# 10
open('temp.txt', 'rb').read()       # BOM 기록
# b'\xef\xbb\xbfspam\nSPAM\n'

open('temp.txt', 'r').read()
# 'ï»¿spam\nSPAM\n'
open('temp.txt', 'r', encoding='utf-8').read()        # BOM 유지
# '\ufeffspam\nSPAM\n'
open('temp.txt', 'r', encoding='utf-8-sig').read()    # BOM 건너뛰기
# 'spam\nSPAM\n'


open('temp.txt', 'w').write('spam\nSPAM\n')
# 10
open('temp.txt', 'rb').read()       # BOM 없는 데이터
# b'spam\r\nSPAM\r\n'

open('temp.txt', 'r').read()        # utf-8로 동작
# 'spam\nSPAM\n'
open('temp.txt', 'r', encoding='utf-8').read()
# 'spam\nSPAM\n'
open('temp.txt', 'r', encoding='utf-8-sig').read()
# 'spam\nSPAM\n'


sys.byteorder
# 'little'
open('temp.txt', 'w', encoding='utf-16').write('spam\nSPAM\n')
# 10
open('temp.txt', 'rb').read()
# b'\xff\xfes\x00p\x00a\x00m\x00\r\x00\n\x00S\x00P\x00A\x00M\x00\r\x00\n\x00'
open('temp.txt', 'r', encoding='utf-16').read()
# 'spam\nSPAM\n'


open('temp.txt', 'w', encoding='utf-16-be').write('\ufeffspam\nSPAM\n')
# 11
open('temp.txt', 'rb').read()
# b'\xfe\xff\x00s\x00p\x00a\x00m\x00\r\x00\n\x00S\x00P\x00A\x00M\x00\r\x00\n'
open('temp.txt', 'r', encoding='utf-16').read()
# 'spam\nSPAM\n'
open('temp.txt', 'r', encoding='utf-16-be').read()
# '\ufeffspam\nSPAM\n'


open('temp.txt', 'w', encoding='utf-16-le').write('SPAM')
# 4
open('temp.txt', 'rb').read()       # BOM이 없거나 필요하다면 OK
b'S\x00P\x00A\x00M\x00'
open('temp.txt', 'r', encoding='utf-16-le').read()
# 'SPAM'
open('temp.txt', 'r', encoding='utf-16').read()
# UnicodeError: UTF-16 stream does not start with BOM
