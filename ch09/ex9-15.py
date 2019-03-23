# 비교, 동등 그리고 진리

L1 = [1, ('a', 3)]              # 같은 값을 가진 별도의 객체
L2 = [1, ('a', 3)]
L1 == L2, L1 is L2              # 동등? 같은 객체?
# (True, False)


S1 = 'spam'
S2 = 'spam'
S1 == S2, S1 is S2
# (True, True)


S1 = 'a longer string'
S2 = 'a longer string'
S1 == S2, S1 is S2
# (True, False)


L1 = [1, ('a', 3)]
L2 = [1, ('a', 2)]
L1 < L2, L1 == L2, L1 > L2      # 작거나, 같너가 크거나: 결과는 튜플
# (False, False, True)
