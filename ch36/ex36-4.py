# 예외가 항상 에러인 것은 아님

while True:
    try:
        line = input()          # stdin으로부터 줄을 읽어 들임(2.X: raw_input)
    except EOFError:
        break                   # 파일 맨 끝에서 루프 종료
    else:
        ...여기서 다음 줄 실행...
