# map이 빠른 경우와 PyPy가 느린 경우

# pybench_cases2.py

pythons += [
    (1, 'C:\python32\python'),
    (0, 'C:pypy\pypy-2.0-beta1\pypy')]

stmts += [
# 함수 호출 사용: map이 가장 빠름
    (0, 0, "[ord(x) for x in 'spam' * 2500]"),
    (0, 0, "res=[]\nfor x in 'spam' * 2500: res.append(ord(x))"),
    (0, 0, "$listif3(map(ord, 'spam' * 2500))"),
    (0, 0, "list(ord(x) for x in 'spam' * 2500)"),
# 집합과 딕셔너리
    (0, 0, "{x ** 2 for x in range(1000)}"),
    (0, 0, "s=set()\nfor x in range(1000): s.add(x ** 2)"),
    (0, 0, "{x: x ** 2 for x in range(1000)}"),
    (0, 0, "d={}\nfor x in range(1000): d[x] = x ** 2"),
# 30만 자릿수
    (1, 1, "len(str(2**1000000))")] # Pypy에서 느린 연산
