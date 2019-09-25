# -*- coding: utf-8 -*-
# 내장된 리스트 타입/클래스를 서브클래스로 만들기
# 1..N을 0..N-1로 매핑하기: 내장된 버전을 다시 호출

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)

if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')           # __init__는 list로부터 상속받음
    print(x)                    # __repr__은 list로부터 상속받음

    print(x[1])                 # MyList.__getitem__
    print(x[3])                 # list 슈퍼클래스의 메서드를 변경

    x.append('spam'); print(x)  # list 슈퍼클래스의 속성
    x.reverse();      print(x)
