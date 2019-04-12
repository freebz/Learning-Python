# 증강 할당

X = X + Y                       # 기존 형식
X += Y                          # 새로운 증강 형식


x = 1
x = x + 1                       # 기존 형식
x
# 2
x += 1                          # 증강 형식
x
# 3


S = "spam"
S += "SPAM"                     # 묵시적인 연결
S
# 'spamSPAM'


L = [1, 2]
L = L + [3]                     # 연결: 느림
L
# [1, 2, 3]
L.append(4)                     # 빠르지만. 직접 변경
L
# [1, 2, 3, 4]


L = L + [5, 6]                  # 연결: 느림
L
# [1, 2, 3, 4, 5, 6]
L.extend([7, 8])                # 빠르지만, 직접 변경
L
# [1, 2, 3, 4, 5, 6, 7, 8]


L += [9, 10]                    # L.extend([9, 10])으로 연결됨
L
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


L = []
L += 'spam'                     # +=와 extend는 모든 시퀀스를 허용하지만 +는 그렇지 않음
L
# ['s', 'p', 'a', 'm']
L = L + 'spam'
# TypeError: can only concatenate list (not "str") to list
