# 객체 지향 프로그래밍(OOP)
# 장점 : 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트 등
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Kim
    Date : 2024.04.18
    """

    # 클래스 변수, 모든 인스턴스가 공유
    car_count = 0

    def __init__(self, company, detail):  # constructor 역할
        self._company = company
        # self.car_count = 10  # 클래스 변수와 동일한 인스턴스의 변수가 있다면 이것이 더 우선순위가 됨
        self._detail = detail
        Car.car_count += 1

    def __str__(self):
        return f'str : {self._company} - {self._detail}'

    def __repr__(self):
        return f'repr : {self._company} - {self._detail}'

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print(f'Current ID: {id(self)}')
        print(f'Car Detail Info : {self._company} {self._detail.get('price')}')


# Self 의미
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'silver', 'horsepower': 300, 'price': 6000})

# ID 확인 - 모두 다름
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)  # False
print(car1 is car2)  # False

# dir & __dict__ 확인
print(dir(car1))
print(dir(car2))

print()
print()

# 인스턴스의 속성 확인
print(car1.__dict__)
print(car2.__dict__)

# Doctring, 문서화
print(Car.__doc__)

print()

# 실행
car1.detail_info()
car2.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__), id(car3.__class__))  # 클래스의 ID 값은 동일하다

# 에러
# Car.detail_info()  # TypeError: Car.detail_info() missing 1 required positional argument: 'self'
Car.detail_info(car3)

print()
print()

# 공유확인
print(car1.car_count)  # 클래스 변수 print
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

# 삭제
del car2
# 삭제 확인
print(car1.car_count)
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모클래스 변수))
