# try/except/else 구문

try:
    statements                  # 이 코드를 먼저 실행
except name1:
    statements                  # try 블록 안에서 name1 예외 발생 시 실행
except (name2, name3):
    statements                  # 괄호 안의 예외 중 하나라도 발생했을 경우 실행
except name4 as var:
    statements                  # name4 예외 발생 시, 예외 인스턴스를 var 변수에 저장 후 실행
except:
    statements                  # 위에서 캐치한 것 이외의 모든 예외에 대해 실행
else:
    statements                  # try 블록 안에서 예외가 발생하지 않았을 경우 실행
