# 객체 지향 프로그래밍(OOP)
# 장점 : 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트 등
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Kim
    Date : 2024.04.18
    Description : Class, Static, Instance Method
                Class : cls를 받아 처리한다
                Instance : self를 받아 처리한다
                Static : parameter를 따로 받지 않아 유연하게 사용한다
    """

    # 클래스 변수, 모든 인스턴스가 공유
    price_per_raise = 1.0

    def __init__(self, company, details):  # constructor 역할
        self._company = company
        self._details = details

    def __str__(self):
        return f'str : {self._company} - {self._details}'

    def __repr__(self):
        return f'repr : {self._company} - {self._details}'

    # Instance Method
    # Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print(f'Current ID: {id(self)}')
        print(f'Car Detail Info : {self._company} {self._details.get('price')}')

    # Instance Method
    def get_price(self):
        return f'Before Car Price -> company : {self._company}, price : {self._details.get('price')}'

    # Instance Method
    def get_price_calc(self):
        return f'After Car Price -> company : {self._company}, price : {self._details.get('price') * Car.price_per_raise}'

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! Price increased')

    # Static Method
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return f'Ok! This car is {inst._company}'
        else:
            return 'Sorry. This car is not BMW'


# Self 의미
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})

# 전체 정보
print('인스턴스의 전체 정보')
car1.detail_info()
car2.detail_info()

print()

# 가격 정보(직접 접근)
print('가격 정보')
print(car1._details.get('price'))

print()

print('<<<< Instance Method')

# 가격 정보(인상 전)
print('가격 인상 전')
print(car1.get_price())
print(car2.get_price())

print()

# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격 정보(인상 후)
print('가격 인상 후')
print(car1.get_price_calc())
print(car2.get_price_calc())

print()

print('<<<< Class Method')

# 클래스 접근
Car.raise_price(1.6)
print('가격 인상 후')
print(car1.get_price_calc())
print(car2.get_price_calc())

print()

print('<<<< Static Method')

# 정적 메서드 접근
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
