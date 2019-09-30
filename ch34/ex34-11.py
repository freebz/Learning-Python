# 중첩을 이용해 finally와 except 조합하기

try:                            # 병합된 형태와 동등한 효과를 갖는 중첩 형태
    try:
        main-action
    except Exception1:
        handler1
        excpet Exception2:
        handler2
    ...
    else:
        no-error
finally:
    cleanup
