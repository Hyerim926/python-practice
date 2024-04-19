# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Interator), 함수(Functions), 클래스(Class)

# Magic Method 란
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# general tuple
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt  # root

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# named tuple
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

# class 형식과 유사
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)  # Point(x=1.0, y=5.0)
print(pt4)  # Point(x=2.5, y=1.5)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
# Type names and field names cannot be a keyword: 'class' / class는 예약어이기 때문에 안됨 -> rename 옵션 값을 주는 것으로 해결 가능
# key 값은 유일해야하기 때문에 rename 옵션으로 새로 생성한다
Point4 = namedtuple('Point', 'x y x class', rename=True)

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(46, y=20)
# rename
p4 = Point4(10, 20, 30, 40)
# unpacking
p5 = Point3(**temp_dict)

print(p1)
print(p2)
print(p3)
print(p4)  # Point(x=10, y=20, _2=30, _3=40)
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# unpacking
x, y = p3
print(x, y)

# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 네임드 튜플 객체 생성
p4 = Point1._make(temp)
print(p4)  # Point(x=52, y=38)

# _fields() : 필드 네밍 확인
print(p1._fields, p2._fields, p3._fields)  # ('x', 'y') ('x', 'y') ('x', 'y')

# _asdict() : OrderedDict 반환
print(p1._asdict())
print(p4._asdict())

# 실 사용 실습
# 한 반에 20명 학생, 4개의 반(A,B,C,D) B14, C20

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

# 추천
students2 = [
    Classes(rank, number)
    for rank in 'A B C D'.split()
    for number in [str(n)
                   for n in range(1, 21)]]

print(len(students2))
print(students2)

# 출력
for s in students:
    print(s)

for s in students2:
    print(f'student {s.rank}{s.number}')
