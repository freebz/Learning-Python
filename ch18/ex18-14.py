# 왜 키워드 전용 인수인가?

process(X, Y, Z)                # 플래그 기본값 사용
process(X, Y, notify=True)      # 플래그 기본값 무시


def process(*args, notify=False): ...
