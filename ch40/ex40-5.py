# 메타클래스 선언

# 3.X에서의 선언

class Spam(metaclass=Meta):             # 3.X 버전에서만


class Spam(Eggs, metaclass=Meta):       # 일반 슈퍼클래스면 OK: 제일 처음 열거되어야 함
