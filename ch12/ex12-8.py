# if/else 삼중 표현식

if X:
    A = Y
else:
    A = Z


A = Y if X else Z


A = 't' if 'spam' else 'f'      # 문자열의 경우 비어 있지 않으면 참
A
# 't'
A = 't' if '' else 'f'
A
# 'f'


A = ((X and Y) or Z)


A = Y if X else Z


A = [Z, y][bool(X)]


['f', 't'][bool('')]
# 'f'
['f', 't'][bool('spam')]
# 't'
