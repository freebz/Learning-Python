X = 11                          # 내 X: 이 파일에서만 전역

import moda                     # moda의 이름들에 대한 접근 권한을 갖게 됨
moda.f()                        # 이 파일의 X가 아니라 moda.X를 설정
print(X, moda.X)


# pythonb modb.py
# 11 99
