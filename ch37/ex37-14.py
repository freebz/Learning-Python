# 소스 파일 문자 집합 인코딩 선언

# -*- coding: latin-1 -*-


# -*- coding: latin-1 -*-
# 다음의 모든 문자열 리터럴 형태는 latin-1 형태로 동작함
# 위의 인코딩을 아스키나 utf-8로 변경하려 하면 오류가 발생하는데,
# myStr1의 0xc4와 0xe8이 아스키나 utf-8에서 유효한 문자가 아니기 때문임

myStr1 = 'aÄBèC'

myStr2 = 'A\u00c4B\U000000e8C'

myStr3 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

import sys
print('Default encoding:', sys.getdefaultencoding())

for aStr in myStr1, myStr2, myStr3:
    print('{0}, strlen={1}, '.format(aStr, len(aStr)), end='')

    bytes1 = aStr.encode()             # 기본 utf-8에 의해 인코드됨. 아스키가 아닌 문자는 2바이트
    bytes2 = aStr.encode('latin-1')    # 한 문자당 1바이트
   #bytes3 = aStr.encode('ascii')      # 아스키는 변환되지 않음. 0-127 범위를 벗어남

    print('byteslen1={0}, byteslen2={1}'.format(len(bytes1), len(bytes2)))


# py -3
# Default encoding: utf-8
# aÄBèC, strlen=5, byteslen1=7, byteslen2=5
# AÄBèC, strlen=5, byteslen1=7, byteslen2=5
# AÄBèC, strlen=5, byteslen1=7, byteslen2=5
