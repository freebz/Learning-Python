# 문자열의 실제 동작

# 기본 동작

len('abc')                      # 길이: 아이템 수
# 3
'abc' + 'def'                   # 연결: 새로운 문자열 생성
# 'abcdef'
'Ni!' * 4                       # 반복: 'Ni!' + 'Ni!' + ...와 같음
# 'Ni!Ni!Ni!Ni!'


print('------ ...생략... ---')  # 80대시. 어려운 방법
print('-' * 80)                 # 80대시. 쉬운 방법


myjob = "hacker"
for c in myjob: print(c, end=' ') # 아이템들을 반복하여 각각 출력(3.X 형식)

# h a c k e r
"k" in myjob                    # 발견됨
# True
"z" in myjob                    # 발견되지 않음
# False
'spam' in 'abcspamdef'          # 부분 문자열 검색. 위치가 반환되지 않음
# True
