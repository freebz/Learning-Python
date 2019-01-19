# 왜 집합인가?

L = [1, 2, 1, 3, 2, 4, 5]
set(L)
# {1, 2, 3, 4, 5}
L = list(set(L))                # 중복 제거
L
# [1, 2, 3, 4, 5]

list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])) # 순서가 변경될 수 있음
# ['cc', 'xx', 'yy', 'dd', 'aa']


set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]) # 리스트의 차이
# {3, 7}
set('abcdefg') - set('abdghij')          # 문자열의 차이
# {'c', 'e', 'f'}
set('spam') - set(['h', 'a', 'm'])       # 혼합 타입의 차이
# {'p', 's'}

set(dir(bytes)) - set(dir(bytearray))    # bytes에 있고 bytearray에는 없는 것
# {'__getnewargs__'}
set(dir(bytearray)) - set(dir(bytes))
# {'copy', '__iadd__', '__setitem__', '__imul__', '__delitem__', '__alloc__', 'reverse', 'insert', 'append', 'extend', 'remove', 'pop', 'clear'}


L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
L1 == L2                        # 순서가 장요한 시퀀스
# False
set(L1) == set(L2)              # 순서에 상관없는 비교
# True
sorted(L1) == sorted(L2)        # 정렬된 리스트의 비교
# True
'spam' == 'asmp', set('spam') == set('asmp'), sorted('spam') == sorted('asmp')
# (False, True, True)


engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}

'bob' in engineers              # bob은 엔지니어인가?
# True

engineers & managers            # 엔지니어이면서 매니저인 사람?
# {'sue'}

engineers | managers            # 한쪽이라도 포함된 모든 사람
# {'bob', 'tom', 'sue', 'vic', 'ann'}

engineers - managers            # 매니저를 제외한 순수 엔지니어
# {'vic', 'ann', 'bob'}

managers - engineers            # 엔지니어를 제외한 순수 매니저
# {'tom'}

engineers > managers            # 모든 엔지니어는 매니저인가?(포함 집합)
# False

{'bob', 'sue'} < engineers      # 두 사람은 엔지니어인가?(부분 집합)
# True

(managers | engineers) > managers # 모든 사람은 매니저의 포함 집합
# True

managers ^ engineers            # 어느 한쪽에만 포함된 사람들?
# {'tom', 'vic', 'ann', 'bob'}

(managers | engineers) - (managers ^ engineers)    # 교집합!
# {'sue'}
