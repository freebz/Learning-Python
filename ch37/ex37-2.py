# 문자열 코딩 기초

# 파이썬 3.X 문자열 리터럴

# py -3
B = b'spam'                   # 3.X의 바이트 리터럴은 bytes 객체 생성(8비트 바이트)
S = 'eggs'                    # 3.X의 str 리터럴은 유니코드 텍스트 문자열 생성

type(B), type(S)
# (<class 'bytes'>, <class 'str'>)

B                             # bytes: 정수의 시퀀스로, 캐릭터 문자열로 출력됨
# b'spam'
S
# 'eggs'


B[0], S[0]   # bytes에서는 인덱스 접근이 정수를 반환하고, 문자열에서는 문자열을 반환함
# (115, 'e')
B[1:], S[1:]    # 슬라이싱은 또 다른 bytes나 str 객체 생성
# (b'pam', 'ggs')
list(B), list(S)
# ([115, 112, 97, 109], ['e', 'g', 'g', 's'])  # bytes는 실제로 8비트 small int임


B[0] = 'x'                      # 둘 다 변형 불가능함
# TypeError: 'bytes' object does not support item assignment
S[0] = 'x'
# TypeError: 'str' object does not support item assignment


# bytes 접두어는 단일, 이중, 삼중, 그리고 raw 리터럴에서 모두 동작함
B = B"""
xxxx
yyyy
"""
B
# b'\nxxxx\nyyyy\n'
