# 불변 제약과 프로즌 집합

S
# {1.23}
S.add([1, 2, 3])                # 집합은 불변 객체만 동작함
# TypeError: unhashable type: 'list'
S.add({'a':1})
# TypeError: unhashable type: 'dict'
S.add((1, 2, 3))
S                               # 리스트와 딕셔너리를 제와한 튜플만 추가할 수 있음
# {1.23, (1, 2, 3)}

S | {(4, 5, 6), (1, 2, 3)}      # 합집합: S.union(...)과 동일
# {1.23, (4, 5, 6), (1, 2, 3)}
(1, 2, 3) in S                  # 멤버십: 완전한 값에 의한 비교
# True
(1, 4, 3) in S
# False
