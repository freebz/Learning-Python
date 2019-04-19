# for 루프

# 일반적인 형식

for target in object:           # 객체의 항목들 대상에 할당
    statements                  # 반복되는 루프 본문: 대상을 활용
else:                           # 선택적인 else 부분
    statements                  # break를 실행하지 않은 경우에 실행


for target in object:           # 객체 항목들을 대상에 할당
    statements
    if test: break              # 루프 즉시 종료. else 미실행
    if test: continue           # 루프 상단으로 즉시 이동
else:
    statements                  # break를 실행하지 않은 경우
