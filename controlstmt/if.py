# 조건문
# IF

# 기본 형식
print(type(True))  # 0이 아닌 수, string, 데이터가 있는 리스트/튜플/딕셔너리
print(type(False))  # 0, 빈 문자열, 빈 리스트/튜플/딕셔너리

# 예제 1
if True:
    print('Good')

if False:
    print('Bad')

# 예제 2
if False:
    print('Bad!')
else:
    print('Good')

print()

# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10

# 양변이 같을 경우
print(x == y)

# 양변이 다를 경우
print(x != y)

# 왼쪽이 클 때 참
print(x > y)

# 왼쪽이 크거나 같을 때 참
print(x >= y)

# 오른쪽이 클 때 참
print(x < y)

# 오른쪽이 크거나 같을 때 참
print(x <= y)

print()

# 예제 3
city = ''
if city:
    print('You are in: ', city)
else:
    print('Please enter your city')

print()

# 예제 4
city2 = 'Seoul'
if city2:
    print('You are in: ', city2)
else:
    print('Please enter your city')

print()

# 논리연산자(중요)
# and, or, not
a = 75
b = 40
c = 50

print('and: ', a > b and b > c)  # a > b > c
print('or: ', a > b or b > c)
print('not: ', not a > b)
print('not: ', not b > c)
print(not True)
print(not False)

print()

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print('e1: ', 3 + 12 > 7 + 3)
print('e2: ', 5 + 10 * 3 > 7 + 3 * 20)
print('e3: ', 5 + 10 > 3 and 7 + 3 == 10)
print('e4: ', 5 + 10 > 0 and not 7 + 3 == 10)

print()

score1 = 90
score2 = 'A'

# 예제 5
# 복수의 조건이 모두 참일 경우에 실행
if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')

print()

# 예제 6
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum':
    print('최상위 관리자')

print()

# 예제 6
# 다중 조건문
num = 90
if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

print()

# 예제 7
# 중첩 조건문
grade = 'A'
total = 90
if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')

print()

# 예제 8
# in, not in
q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {
    'name': 'Lee',
    'city': 'Seoul',
    'grade': 'A'
}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print('name' in e)
print('seoul' in e.values())
