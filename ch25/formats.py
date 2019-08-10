# -*- coding: utf8 -*-
#!python
"""
파일: formats.py(2.X and 3.X)
다양하게 특화된 문자열 표시 포매팅 도구.
안에 포함된 셀프 테스트 또는 명령 라인 인수로 테스트해 볼 것
할 일: 음수 money를 위해 parens를 추가하고, 더 많은 특징들 추가할 것
"""

def commas(N):
    """
    양의 정수 같은 N을 출력하기 위해 쉼표로 자릿수를 그룹핑하여 포맷을 맞춤: "xxx.yyy.zzz"
    """
    digits = str(N)
    assert digits.isdigit()
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result

def money(N, numwidth=0, currency='$'):
    """
    숫자 N을 자릿수 구분을 위한 쉼표와 소수점 두 자리로 표시하고,
    그 앞에는 $와 부호 그리고 선택적인 메우기(padding)를 사용함: "$ -xxx.yyy.zz".
    공간 메우기가 없는 경우 numwidth = 0. 기호를 생략하려면 currency = ''.
    그리고 다른 코드를 위해 아스키가 아닌 문자를 사용(예 pound = u'\xA3' or u'\u00A3').
    """
    sign = '-' if N < 0 else ''
    N = abs(N)
    whole = commas(int(N))
    fract = ('%.2f' % N)[-2:]
    number = '%s%s.%s' % (sign, whole, fract)
    return '%s%*s' % (currency, numwidth, number)

if __name__ == '__main__':
    def selftest():
        tests = 0, 1 # fails: -1. 1.23
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))

        print('')
        tests = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.345, 12.346
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2, 0.2345
        tests += -1.2345, -1.2, -0.2345
        tests += -(2 ** 32), -(2**32 + .2345)
        tests += (2 ** 100), -(2 ** 100)
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))

    import sys
    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))
