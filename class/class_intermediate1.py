# 객체 지향 프로그래밍(OOP)
# 장점 : 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트 등
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩
# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량2
car_company_2 = 'BMW'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'silver'},
    {'horsepower': 300},
    {'price': 6000}
]

# 리스트 구조
# 관리가 용이하지 않음
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'silver', 'horsepower': 300, 'price': 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등
car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'BMW', 'car_detail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'silver', 'horsepower': 300, 'price': 6000}},
]

del car_dicts[1]
print(car_dicts)

print()
print()


# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
    def __init__(self, company, detail):  # constructor 역할
        self._company = company
        self._detail = detail

    # 인스턴스 생성 후 인스턴스를 print 할 때 보여주기 위한 함수 (기본은 객체의 타입과 id값을 반환함)
    # str과 repr 중에서는 우선순위가 더 높다
    # str : 사용자 레벨로 객체 정보 확인
    def __str__(self):
        return f'str : {self._company} - {self._detail}'

    # repr : 개발자 레벨로 객체 정보 확인
    def __repr__(self):
        return f'repr : {self._company} - {self._detail}'


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'silver', 'horsepower': 300, 'price': 6000})
print(car1)
print(car2)
print(car3)

print()

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print()
print()

# 리스트 선언
car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)  # 리스트 안에서 객체에 대한 정보를 보여주기 때문에 __repr__ 이 호출됨

print()
print()

for car in car_list:
    print(car)  # 반복(__str__)
    print(repr(car))
