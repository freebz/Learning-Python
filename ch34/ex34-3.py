# 모든 예외 캐치하기: 빈 except절과 예외

try:
    action()
except NameError:
    ...                         # NameError를 처리
except IndexError:
    ...                         # IndexError를 처리
except:
    ...                         # 기타 다른 예외를 처리
else:
    ...                         # 예외가 발생하지 않은 경우를 처리


try:
    action()
except:
    ...                         # 발생할 수 있는 모든 예외를 잡아냄


try:
    action()
except Exception:
    ...                         # exits를 제외한 모든 예외를 잡아냄
