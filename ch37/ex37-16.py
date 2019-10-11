# 시퀀스 연산

B = b'spam'                     # small int의 시퀀스
B
# b'spam'

B[0]                            # 인덱싱은 정수를 반환함
# 115
B[-1]
# 109

chr(B[0])                       # 정수에 해당하는 문자를 표시함
# 's'

list(B)                         # 모든 바이트에 대한 정수값을 표시함
# [115, 112, 97, 109]

B[1:], B[:-1]
# (b'pam', b'spa')
len(B)
# 4
B + b'lmn'
# b'spamlmn'
B * 4
# b'spamspamspamspam'
