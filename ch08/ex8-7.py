# 또 다른 리스트 메서드

L = [1, 2]
L.extend([3, 4, 5])             # 다수의 아이템을 끝에 추가(직접 변경하는 +와 같음)
L
# [1, 2, 3, 4, 5]
L.pop()                         # 마지막 아이템을 삭제하고 반환(기본값은:-1)
# 5
L
# [1, 2, 3, 4]
L.reverse()                     # 직접 변경하는 순서를 반대로 바꾸는 메서드
L
# [4, 3, 2, 1]
list(reversed(L))               # 결과를 다시 내장 함수로 뒤집기
# [1, 2, 3, 4]


L = []
L.append(1)                     # 스택에 밀어 넣기
L.append(2)
L
# [1, 2]
L.pop()                         # 스택에서 꺼내기
# 2
L
# [1]


L = ['spam', 'eggs', 'ham']
L.index('eggs')                 # 객체의 인덱스
# 1
L.insert(1, 'toast')            # 특정 위치에 삽입
L
# ['spam', 'toast', 'eggs', 'ham']
L.remove('eggs')                # 해당 값을 삭제
L
# ['spam', 'toast', 'ham']
L.pop(1)                        # 특정 위치에 값 삭제
# 'toast'
L
# ['spam', 'ham']
L.count('spam')                 # 발생 수
# 1
