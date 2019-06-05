# 키워드 인수와 기본값 조합하기

def func(spam, eggs, toast=0, ham=0): # 처음 두 개는 필수
    print((spam, eggs, toast, ham))

func(1, 2)                      # 결과: (1, 2, 0, 0)
func(1, ham=1, eggs=0)          # 결과: (1, 0, 0, 1)
func(spam=1, eggs=0)            # 결과: (1, 0, 0, 0)
func(toast=1, eggs=2, spam=3)   # 결과: (3, 2, 1, 0)
func(1, 2, 3, 4)                # 결과: (1, 2, 3, 4)
