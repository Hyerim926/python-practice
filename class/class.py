# 클래스
# 붕어빵 틀
# OOP 객체 지향 프로그램
# self, 인스턴스 메서드, 인스턴스 변수

# 클래스와 인스턴스의 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간 (딕셔너리 형태로 사용 가능)
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제 1
class Dog:  # object 상속 받음
    # 클래스 속성 (공유하는 공간)
    species = 'firstdog'

    # 초기화/인스턴스 속성 (나만의 공간)
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 클래스 정보
print(Dog)  # <class '__main__.Dog'>

# 인스턴스화, 생성된 인스턴스는 값이 같아도 다 다르다
a = Dog('jaerong', 11)
b = Dog('dambi', 6)
c = Dog('dambi', 6)  # b와 주소값 다름

# 비교
print(a == b, id(a), id(b), id(c))

# 네임스페이스 / 인스턴스를 딕셔너리로 확인
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

# 클래스 속성에 직접 접근
if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

print()


# 예제2
# self의 이해
class SelfTest:
    # __init__ 메서드를 선언하지 않으면 파이썬 내부적으로 실행해준다

    # 클래스 메서드 - 클래스로 접근해야함
    def func1():
        print('Func1 called')

    # 인스턴스 메서드 - 인스턴스로 접근해야함
    def func2(self):
        print(id(self))
        print('Func2 called')


f = SelfTest()

print(dir(f))
print(id(f))

# 인스턴스로 접근해서 호출하면 인자가 없어서 에러가 발생
# f.func1()  # TypeError: SelfTest.func1() takes 0 positional arguments but 1 was given
# 방법
SelfTest.func1()

f.func2()
# 클래스로 바로 접근해서 호출하면 인자가 없어서 에러가 발생
# SelfTest.func2()  # TypeError: SelfTest.func2() missing 1 required positional argument: 'self'

print()


# 예제 3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 = 0
    # 붕어빵 기계로 붕어빵 몇개 구웠느지
    stock_num = 0  # 재고

    # 객체 초기화 (생성자)
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    # 객체가 소멸할 때 자동으로 삭제되는 메서드 (소멸자)
    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Lee')
user2 = Warehouse('Joe')

print(Warehouse.stock_num)

# Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)  # 인스턴스 내부에 없으면 클래스의 네임스페이스에서 찾음

del user1
print('after', Warehouse.__dict__)

print()

# 예제 4
class Dog:  # object 상속 받음
    # 클래스 속성 (공유하는 공간)
    species = 'firstdog'

    # 초기화/인스턴스 속성 (나만의 공간)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

dog1 = Dog('Kee', 13)
dog2 = Dog('Kevin', 5)
print(dog1.info())
print(dog2.info())

print(dog1.speak('bowwow'))
print(dog2.speak('walwal'))