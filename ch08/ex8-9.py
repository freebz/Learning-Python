# 딕셔너리

# 딕셔너리의 동작

# 기본 딕셔너리 연산

D = {'spam': 2, 'ham': 1, 'eggs': 3} # 딕셔너리 생성
D['spam']                            # 키로 값을 가져오기
# 2
D                                    # 정렬 순서는 뒤섞여 있음
# {'spam': 2, 'ham': 1, 'eggs': 3}


len(D)                          # 딕셔너리의 항목 수
# 3
'ham' in D                      # 또 다른 키 맴버쉽 테스트
# True
list(D.keys())                  # 딕셔너리 D의 키로 새로운 리스트 생성
# ['spam', 'ham', 'eggs']
