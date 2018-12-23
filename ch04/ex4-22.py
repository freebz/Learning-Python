# 유니코드 텍스트 파일

S = 'sp\xc4m'                                          # 아스키가 아닌 유니코드 텍스트
S
# 'spÄm'
S[2]                                                   # 문자들의 시퀀스
# 'Ä'

file = open('unidata.txt', 'w', encoding='utf-8')      # UTF-8 인코딩으로 쓰기
file.write(S)                                          # 4문자 쓰기
# 4
file.close()

text = open('unidata.txt', encoding='utf-8').read()    # UTF-8 텍스트 읽기/디코딩
text
# 'spÄm'
len(text)                                              # 4문자(코드 포인트)
# 4


raw = open('unidata.txt', 'rb').read()                 # 인코딩된 원시 바이트 읽기
raw
# b'sp\xc3\x84m'
len(raw)                                               # 실제 UTF-8로 5바이트
# 5


text.encode('utf-8')                                   # 바이트로 수동 인코딩
# b'sp\xc3\x84m'
raw.decode('utf-8')                                    # str로 수동 디코딩
# 'spÄm'


text.encode('latin-1')                                 # 다른 인코딩을 사용한 바이트
# b'sp\xc4m'
text.encode('utf-16')
# b'\xff\xfes\x00p\x00\xc4\x00m\x00'

len(text.encode('latin-1')), len(text.encode('utf-16'))
# (4, 10)

b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16')    # 같은 문자열로 디코딩
# 'spÄm'


import codecs
codecs.open('unidata.txt', encoding='utf8').read()     # 2.X: 텍스트를 읽고 디코딩
# u'sp\xc4m'
open('unidata.txt', 'rb').read()    # 2.X: 원시 바이트 읽기
# 'sp\xc3\x84m'
open('unidata.txt').read()          # 2.X: 위와 같은 디코딩되지 않은 원시 바이트
# 'sp\xc3\x84m'
