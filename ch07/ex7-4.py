# 삼중 인용 부호를 이용한 멀티라인 블록 문자열

mantra = """Always look
  on the bright
side of life."""

mantra
# 'Always look\n  on the bright\nside of life.'


print(mantra)
# Always look
#   on the bright
# side of life.


menu = """spam                  # 이 주석은 문자열에 추가됨
eggs                            # 위와 같음
"""
menu
# 'spam                  # 이 주석은 문자열에 추가됨\neggs                            # 위와 같음\n'

menu = (
    "spam\n"                    # 이 주석은 무시됨
    "eggs\n"                    # 그러나 자동으로 줄바꿈이 되지 않음
)
menu
# 'spam\neggs\n'


X = 1
"""
import os                       # 이 코드의 실행을 임시로 막음
print(os.getcwd())
"""
Y = 2
