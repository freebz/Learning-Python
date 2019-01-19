# 파이썬 3.X와 2.7에서 집합 컴프리헨션

{x ** 2 for x in [1, 2, 3, 4]}  # 3.X/2.7 집합 컴프리헨션
# {16, 1, 4, 9}


{x for x in 'spam'}             # set('spam')과 동일
# {'m', 's', 'p', 'a'}

{c * 4 for c in 'spam'}         # 표현식 결과의 집합
# {'pppp', 'aaaa', 'ssss', 'mmmm'}
{c * 4 for c in 'spamham'}
#{ 'pppp', 'aaaa', 'hhhh', 'ssss', 'mmmm'}

S = {c * 4 for c in 'spam'}
S | {'mmmm', 'xxxx'}
# {'pppp', 'xxxx', 'mmmm', 'aaaa', 'ssss'}
S & {'mmmm', 'xxxx'}
# {'mmmm'}
