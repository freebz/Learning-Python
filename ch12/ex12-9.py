# 더 생각해 볼 주제: 부울

X = A or B or C or None


X = A or default


if f1() or f2(): ...


tmp1, tmp2 = f1(), f2()
if tmp1 or tmp2: ...


L = [1, 0, 2, 0, 'spam', '', 'ham', []]
list(filter(bool, L))           # 참인 값 구하기
# [1, 2, 'spam', 'ham']
[x for x in L if x]             # 리스트 컴프리헨션
# [1, 2, 'spam', 'ham']
any(L), all(L)                  # 전체적인 진릿값
# (True, False)
