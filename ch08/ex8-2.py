# 리스트 컴프리헨션과 반복

3 in [1, 2, 3]                  # 멤버십
# True
for x in [1, 2, 3]:
    print(x, end=' ')           # 반복(2.X에서는 print x 형태로 사용)

# 1 2 3


res = [c * 4 for c in 'SPAM']   # 리스트 컴프리헨션
    res
# ['SSSS', 'PPPP', 'AAAA', 'MMMM']


res = []
for c in 'SPAM':                # 리스트 컴프리헨션과 같은 기능
    res.append(c * 4)

res
# ['SSSS', 'PPPP', 'AAAA', 'MMMM']


list(map(abs, [-1, -2, 0, 1, 2])) # 시퀀스의 아이템들에 대해 함수 매핑
# [1, 2, 0, 1, 2]
