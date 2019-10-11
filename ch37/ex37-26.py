# 파일 출력 인코딩

# 파일에 기록할 때 자동으로 인코드
open('latindata', 'w', encoding='latin-1').write(S)    # latin-1로 쓰기
# 5
open('utf8data', 'w', encoding='utf-8').write(S)       # utf-8로 쓰기
# 5

open('latindata', 'rb').read()                         # raw 바이트 읽기
# b'A\xc4B\xe8C'

open('utf8data', 'rb').read()                          # 파일마다 내용이 다름
# b'A\xc3\x84B\xc3\xa8C'
