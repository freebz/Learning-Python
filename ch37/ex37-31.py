# 2.X의 유니코드 파일

# py -2
S = u'A\xc4B\xe8C'              # 2.X 타입
print S
# AÄBèC
len(S)
# 5
S.encode('latin-1')                                         # 수동 호출
# 'A\xc4B\xe8C'

import codecs                                               # 2.X 파일

codecs.open('latindata', 'w', encoding='latin-1').write(S)  # 인코드한 값을 기록
codecs.open('utfdata', 'w', encoding='utf-8').write(S)

open('latindata', 'rb').read()
# 'A\xc4B\xe8C'
open('utfdata', 'rb').read()
# 'A\xc3\x84B\xc3\xa8C'

codecs.open('latindata', 'r', encoding='latin-1').read()    # 디코드한 값을 읽음
# u'A\xc4B\xe8C'
codecs.open('utfdata', 'r', encoding='utf-8').read()
# u'A\xc4B\xe8C'
print codecs.open('utfdata', 'r', encoding='utf-8').read()  # 출력하여 보기
# AÄBèC
