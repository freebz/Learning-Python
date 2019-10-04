# 너무 적게 잡아내는 것: 클래스 기반의 카테고리 사용하기

try:
    ...
except (MyExcept1, MyExcept2):  # 이후에 MyExcept3가 여기에 추가되면 Break!
    ...                         # 에러가 아님
else:
    ...                         # 에러로 가정


try:
    ...
except SuccessCategoryName:     # MyExcept3 서브클래스를 나중에 추가한다면 OK
    ...                         # 에러가 아님
else:
    ...                         # 에러로 가정
