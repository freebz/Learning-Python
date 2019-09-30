# 통합된 try/except/finally

try:                            # 병합된 형태
    main-action
except Exception1:
    handler1
except Exception2:              # 예외 캐치
    handler2
...
else:                           # 예외 처리기 없음
    else-block
finally:                        # fianlly가 다른 모든 것들을 수용함
    finally-block
