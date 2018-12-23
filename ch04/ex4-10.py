# 타입별 연산

L.append('NI')                  # 큭기ㅏ 늘어남: 리스트의 끝에 객체 추가
L
# [123, 'spam', 1.23, 'NI']

L.pop(2)                        # 크기가 줄어듬: 중간 아이템 하나를 제거
# 1.23
L
# [123, 'spam', 'NI']


M = ['bb', 'aa', 'cc']
M.sort()
M
# ['aa', 'bb', 'cc']
M.reverse()
M
# ['cc', 'bb', 'aa']
