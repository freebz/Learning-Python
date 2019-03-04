# 추가 딕셔너리 메서드

D = {'spam': 2, 'ham': 1, 'eggs': 3}
list(D.values())
# [2, 1, 3]
list(D.items())
# [('spam', 2), ('ham', 1), ('eggs', 3)]


D.get('spam')                   # 존재하는 키
# 2
print(D.get('toast'))           # 존재하지 않는 키
# None
D.get('toast', 88)
# 88


D
# {'spam': 2, 'ham': 1, 'eggs': 3}
D2 = {'toast':4, 'muffin':5}    # 뒤섞인 음식 주문
D.update(D2)
D
# {'spam': 2, 'ham': 1, 'eggs': 3, 'toast': 4, 'muffin': 5}


# 키로 딕셔너리에서 꺼내기(pop)
D
# {'spam': 2, 'ham': 1, 'eggs': 3, 'toast': 4, 'muffin': 5}
D.pop('muffin')
# 5
D
# {'spam': 2, 'ham': 1, 'eggs': 3, 'toast': 4}

# 위치로 리스트에서 꺼내기(pop)
L = ['aa', 'bb', 'cc', 'dd']
L.pop()                         # 끝에서 삭제하고 반환
# 'dd'
L
# ['aa', 'bb', 'cc']
L.pop(1)                        # 특정 위치에서 지우기
# 'bb'
L
# ['aa', 'cc']
