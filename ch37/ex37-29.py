# 3.X에서의 BOM 처리

# 메모장으로 BOM 제거하기

# py -3                         # 메모장에 저장된 파일
import sys
sys.getdefaultencoding()
# 'utf-8'
open('spam.txt', 'rb').read()   # 아스키(UTF-8) 텍스트 파일
# b'spam\r\nSPAM\r\n'
open('spam.txt', 'r').read()    # 텍스트 모드의 개행 문자 자동 변환
# 'spam\nSPAM\n'
open('spam.txt', 'r', encoding='utf-8').read()
# 'spam\nSPAM\n'


open('spam.txt', 'rb').read()   # 3바이트 BOM을 가진 UTF-8
# b'\xef\xbb\xbfspam\r\nSPAM\r\n'
open('spam.txt', 'r').read()
# 'ï»¿spam\nSPAM\n'
open('spam.txt', 'r', encoding='utf-8').read()
# '\ufeffspam\nSPAM\n'
open('spam.txt', 'r', encoding='utf-8-sig').read()
# 'spam\nSPAM\n'


open('spam.txt', 'rb').read()
# b'\xfe\xff\x00s\x00p\x00a\x00m\x00\r\x00\n\x00S\x00P\x00A\x00M\x00\r\x00\n'
open('spam.txt', 'r').read()
# b'\xfeÿ\x00s\x00p\x00a\x00m\x00\n\x00\n\x00S\x00P\x00A\x00M\x00\n\x00\n'
open('spam.txt', 'r', encoding='utf-16').read()
# 'spam\nSPAM\n'
open('spam.txt', 'r', encoding='utf-16-be').read()
# '\ufeffspam\nSPAM\n'
