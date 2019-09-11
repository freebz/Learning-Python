# 하지만 3.X의 __index__는 인덱싱이 아님!

class C:
    def __index__(self):
        return 255

X = C()
hex(X)                          # 정숫값
# '0xff'
bin(X)
# '0b11111111'
oct(X)
# '0o377'


('C' * 256)[255]
# 'C'
('C' * 256)[X]                  # 색인(인덱스)으로 사용(X[i]가 아님)
# 'C'
('C' * 256)[X:]                 # 색인(인덱스)으로 사용(X[i:]가 이님)
# 'C'