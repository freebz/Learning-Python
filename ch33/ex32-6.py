# 더 생각해 볼 주제: 오류 확인

doStuff()
{                                   # C 프로그램
    if (doFirstThing() == ERROR)    # 이 함수 내에서 직접 오류를 처리하지 않더라도
        return ERROR;
    if (doNextThing() == ERROR)
        return ERROR;
    ...
    return doLastThing();
}


def doStuff():                  # 파이썬 코드
    doFirstThing()              # 예외에 대해서 신경 쓸 필요가 없으므로
    doNextThing()               # 오류를 탐지할 필요도 없음
    ...
    doLastThing()

if __name__ == '__main__':
    try:
        doStuff()               # 여기서 결과를 확인함
    except:                     # 그러므로 여기서만 오류를 확인하면 됨
        badEnding()
    else:
        goodEnding()
