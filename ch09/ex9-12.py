# 더 생각해 볼 주제: 연산자 오버로딩

class MySequence:
    def __getitem__(self, index):
        # 객체[인덱스]로 호출됨
    def __add__(self, other):
        # 객체 + 다른 객체로 호출됨
    def __iter__(self):
        # 반복 상황에서 호출됨
