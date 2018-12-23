# 불변성

S
# 'Spam'

S[0] = 'z'                      # 불변 객체는 변경할 수 없음
# ... 오류 메시지 생략..
# TypeError: 'str' object does not support item assignment

S = 'z' + S[1:]                 # 하지만 새로운 객체를 생성하는 표현식은 가능
S
# 'zpam'


S = 'shrubbery'
L = list(S)                     # 리스트로 확장 [...]
L
# ['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
L[1] = 'c'                      # 직접 변경
''.join(L)                      # 빈 구분자로 결합
# 'scrubbery'

B = bytearray(b'spam')          # 바이트/리스트가 혼합된 형태
B.extend(b'eggs')               # 'b'는 3.X에서만 필요함
B                               # B[i] = ord(x) 여기서 동일하게 동작
# bytearray(b'spameggs')
B.decode()                      # 일반적인 문자열로 변환
# 'spameggseggs'
