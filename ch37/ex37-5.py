# 문자열 타입 변환

S = 'eggs'
S.encode()                      # str -> bytes; 텍스트를 raw 바이트로 인코딩
# b'eggs'
bytes(S, encoding='ascii')      # str -> bytes, 다른 방법
# b'eggs'

B = b'spam'
B.decode()                      # bytes -> str; raw 바이트를 텍스트로 디코딩
# 'spam'
str(B, encoding='ascii')        # bytes -> str, 다른 방법
# 'spam'


import sys
sys.platform                    # 코드가 동작하는 플랫폼
# 'win32'
sys.getdefaultencoding()        # str의 기본 인코딩 확인
# 'utf-8'

bytes(S)
# TypeError: string argument without an encoding

str(B)                          # 인코딩 인수 없이 str 호출
# "b'spam'"                     # 변환이 아닌 출력 문자열이 표시됨!
len(str(B))
# 7
len(str(B, encoding='ascii'))   # str로 변환할 때 인코딩 인수 사용
# 4


S = 'spam'                      # 2.X 타입 문자열 변환 도구
U = u'eggs'
S, U
# ('spam', u'eggs')
unicode(S), str(U)              # 2.X에서 str -> uni, uni -> str 변환
# (u'spam', 'eggs')
S.decode(), U.encode()          # 3.X의 byte -> str 변환과 str -> bytes 변환
# (u'spam', 'eggs')
