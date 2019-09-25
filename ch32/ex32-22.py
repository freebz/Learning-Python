# __getattribute__와 디스크립터: 속성 도구

class AgeDesc(object):
    def __get__(self, instance, owner): return 40
    def __set__(self, instance, value): instance._age = value

class descriptors(object):
    age = AgeDesc()

x = descriptors()
x.age                           # AgeDesc.__get__ 실행
# 40
x.age = 42                      # AgeDesc.__set__ 실행
x._age                          # 일반 가져오기: AgeDesc 호출하지 않음
# 42
