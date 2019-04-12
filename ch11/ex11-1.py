# 시퀀스 할당

nudge = 1                       # 기본 할당
wink = 2
A, B = nudge, wink              # 튜플 할당
A, B                            # A = nudge, B = wink와 같음
# (1, 2)
[C, D] = [nudge, wink]          # 리스트 할당
C, D
# (1, 2)


nudge = 1
wink = 2
nudge, wink = wink, nudge       # 튜플: 값 교환
nudge, wink                     # T = nudge, nudge = wink, wink = T와 같음
# (2, 1)


[a, b, c] = (1, 2, 3)           # 값들의 튜플을 이름 리스트에 할당
a, c
# (1, 3)
(a, b, c) = "ABC"               # 문자들의 문자열을 튜플에 할당
a, c
# ('A', 'C')
