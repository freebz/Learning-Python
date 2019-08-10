# 문서화 문자열: 실제 작업에서의 모듈 관련 문서

import formats
help(formats)
Help on module formats:

이름
    formats

설명
    파일: formats.py(2.X and 3.X)
    다양하게 특화된 문자열 표시 포매팅 도구.
    안에 포함된 셀프 테스트 또는 명령 라인 인수로 테스트해 볼 것
    할 일: 음수 money를 위해 parens를 추가하고, 더 많은 특징들 추가할 것

함수
    commas(N)
        양의 정수 같은 N을 출력하기 위해 쉼표로 자릿수를 그룹핑하여 포맷을 맞춤: "xxx.yyy.zzz"
    
    money(N, numwidth=0, currency='$')
        숫자 N을 자릿수 구분을 위한 쉼표와 소수점 두 자리로 표시하고,
        그 앞에는 $와 부호 그리고 선택적인 메우기(padding)를 사용함: "$ -xxx.yyy.zz".
        공간 메우기가 없는 경우 numwidth = 0. 기호를 생략하려면 currency = ''.
        그리고 다른 코드를 위해 아스키가 아닌 문자를 사용(예 pound = u'£' or u'£').

파일
    c:\code\formats.py
