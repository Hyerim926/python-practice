# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Interator), 함수(Functions), 클래스(Class)

# Magic Method 란
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 기본형
print('모든 데이터 타입은 클래스이다')
print(int)  # <class 'int'>
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10  # int

print(type(n))

print()

print(n + 100)  # special method 중 __add__ 가 실행됨
print(n.__add__(100))
print(n.__doc__)  # comment 출력
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()


# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f'Fruit Class Info : {self._name} , {self._price}'

    # 클래스방식의 더하기
    def __add__(self, x):
        print('Called >> __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called >> __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('Called >> __le__')
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print('Called >> __ge__')
        if self._price >= x._price:
            return True
        else:
            return False


s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 일반적인 계산
print(s1._price + s2._price)

# 매직 메소드 계산
print(s1 + s2)  # s2가 자동으로 x로 넘어감
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)
print(s2 - s1)
print(s2 + s1)
print(s1)
print(s2)
