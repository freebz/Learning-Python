# 복합 사용 모드: __name__과 __main__

def tester():
    print("It's Christmas in Heaven...")

if __name__ == '__main__':      # 실행될 때만
    tester()                    # 임포트될 때는 해당되지 않음


# python
import runme
runme.tester()
# It's Christmas in Heaven...


# python runme.py
# It's Christmas in Heaven...
