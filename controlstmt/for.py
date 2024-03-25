# 반복문
# for 실습

# for in <collection>
#     <loof body>

for v1 in range(10):  # 0 ~ 9
    print('v1: ', v1)

print()
for v2 in range(1, 11):  # 1 ~ 10
    print('v2: ', v2)

print()

for v3 in range(1, 11, 3):  # 1 ~ 10까지 3간격으로
    print('v3: ', v3)

print()
# 1 ~ 1000 합
sum1 = 0
for v in range(1, 1001):
    sum1 += v

print('1 ~ 1000 sum: ', sum1)

print('1 ~ 1000 sum: ', sum(range(1, 1001)))
print('1 ~ 1000에서 4의 배수의 합 : ', sum(range(1, 1001, 4)))

print()
# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제 1
names = ['John', 'Smith', 'Kim', 'David', 'Ken']
for name1 in names:
    print('You are : ', name1)

print()

# 예제 2
lotto_numbers = [11, 12, 47, 14, 35, 16, 77, 33]
for lotto_number in lotto_numbers:
    print('Current Number: ', lotto_number)

print()

# 예제 3
word = 'Beautiful'
for letter in word:
    print(letter)

print()

# 예제 4
my_info = {
    'name': 'lee',
    'age': 33,
    'city': 'seoul'
}
for key in my_info:
    print('key: ', key)

print()

for value in my_info.values():
    print('value: ', value)

print()

# 예제 5
name = 'PineAppLe'
for letter in name:
    if letter.isupper():
        print(letter)
    else:
        print(letter.upper())

print()

# break
numbers = [14, 27, 34, 49, 56, 64, 71, 89, 94]
for number in numbers:
    if number == 34:
        print('Found : ', number)
        break
    else:
        print('Not found: ', number)

print()

# continue
lt = ['1', 56, True, 4.3, complex(4)]
for el in lt:
    if type(el) is bool:  # 자료형 비교대조할 때는 is/is not 사용
        continue
    print('current type: ', el, type(el))
    print('multiply by 2', el * 2)

print()

# for - else
numbers = [14, 27, 34, 49, 56, 64, 71, 89, 94]
for number in numbers:
    if number == 26:
        print('Found : 26')
        break
else:  # 배열의 모든 원소를 반복하고 마지막으로 출력
    print('Not found: 26')

print()

# 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')
    print()

print()

# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))  # id 값
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))  # set은 순서가 없음