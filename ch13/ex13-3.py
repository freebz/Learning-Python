# break, continue, pass, 그리고 루프 else

# 일반적인 루프 형식

while test:
    statements
    if test: break              # 바로 루프를 빠져나감. else문은 생략
    if test: continue           # 바로 루프의 상단에 있는 테스트로 이동
else:
    statements                  # break를 만나지 않고 루프를 종료할 경우 실행
