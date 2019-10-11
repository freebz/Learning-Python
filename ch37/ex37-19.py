# 파이선 3.X/2.6+에서 bytesarray 객체 사용하기

# bytearray 활용

# 2.6/2.7에서의 초기화: 0-255 범위 small int의 변경 가능한 시퀀스

S = 'spam'
C = bytearray(S)                # 3.X에서 2.6 이상 버전으로 하위 호환 포팅
C                               # 2.6 이상에서 b'..' == '..'(문자열)
# bytearray(b'spam')


# 3.X에서 bytearray 생성: 텍스트와 바이너리 혼용 불가
S = 'spam'
C = bytearray(S)
# TypeError: string argument without an encoding

C = bytearray(S, 'latin1')
C
# bytearray(b'spam')

B = b'spam'                     # 3.X: b'..' != '..'(bytes/str)
C = bytearray(B)
C
# bytearray(b'spam')


# 변형 가능하지만, 문자열이 아닌 정수를 할당해야 함

C[0]
# 115

C[0] = 'x'                      # 이 줄과 다음 줄은 2.6/2.7에서 동작함
# TypeError: 'str' object cannot be interpreted as an integer
C[0] = b'x'
# TypeError: 'bytes' object cannot be interpreted as an integer

C[0] = ord('x')                 # ord()를 이용해 문자의 코드 값을 얻음
C
# bytearray(b'xpam')

C[1] = b'Y'[0]                  # 또는 바이트 문자열을 인덱스함
C
# bytearray(b'xYam')


# bytes에는 있지만, bytearray에 없는 메서드
set(dir(b'abc')) - set(dir(bytearray(b'abc')))
# {'__getnewargs__'}

# bytearray에는 있지만 bytes에는 없는 메서드
set(dir(bytearray(b'abc'))) - set(dir(b'abc'))
# {'pop', 'clear', 'append', '__setitem__', '__alloc__', 'reverse', 'extend', '__imul__', 'copy', '__delitem__', 'remove', '__iadd__', 'insert'}


# 변형 가능한 메서드 호출

C
# bytearray(b'xYam')

C.append(b'LMN')                # 2.X는 크기가 1인 문자열 필요
# TypeError: 'bytes' object cannot be interpreted as an integer

C.append(ord('L'))
C
# bytearray(b'xYamL')

C.extend(b'MNO')
C
# bytearray(b'xYamLMNO')


# 시퀀스 동작 및 문자열 메서드

C
# bytearray(b'xYamLMNO')

C + b'!#'
# bytearray(b'xYamLMNO!#')
C[0]
# 120

C[1:]
# bytearray(b'YamLMNO')
len(C)
# 8

C.replace('xY', 'sp')           # 2.X에서 동작
# TypeError: a bytes-like object is required, not 'str'
C.replace(b'xY', b'sp')
;bytearray(b'spamLMNO')

C
# bytearray(b'xYamLMNO')
C * 4
# bytearray(b'xYamLMNOxYamLMNOxYamLMNOxYamLMNO')
