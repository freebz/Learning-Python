# 기본 사용법

with expression [as variable]:
    with-block


with open(r'C:\misc\data') as myfile:
    for line in myfile:
        print(line)
        ...코드 생략...


myfile = open(r'C:\misc\data')
try:
    for line in myfile:
        print(line)
        ...코드 생략...
finally:
    myfile.close()


lock = threading.Lock()         # 유의: import threading 필요
with lock:
    # 코드의 임계 영역(critical section)
    ...공유 리소스에 접근...


with decimal.localcontext() as ctx:    # 유의: import decimal 필요
    ctx.prec = 2
    x = decimal.Decimal('1.00') / decimal.Decimal('3.00')
