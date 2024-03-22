# 딕셔너리 js의 object/map, 해쉬 테이블
# 범용적으로 가장 많이 사용됨
# 순서x, 키 중복, 수정o, 삭제o

# 선언
# 중괄호 선언법
a = {
    'name': 'Kim',
    1: 'number',
    'phone': '01033337777',
    'birth': '960926'
}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'San Francisco',
    'Age': 29,
    'Grade': 'A',
    'Status': True
}
# 명시적 선언법
e = dict([
    ('Name', 'Niceman'),
    ('City', 'San Francisco'),
    ('Age', 29),
    ('Grade', 'A'),
    ('Status', True),
])

# 선호되는 방식
f = dict(
    Name='Niceman',
    City='San Francisco',
    Age=29,
    Grade='A',
    Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
print('a - ', a['name'])  # 존재 x 키 -> 에러 발생
print('a - ', a.get('name'))  # 존재 x 키 -> None 처리 / optional chaining과 유사
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))
print()

# 딕셔너리 추가
a['address'] = '123 Main St'
print('a - ', a)
a['name'] = 'NewNiceman'  # 값 수정
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)
print()

# 길이 출력 가능, key 개수
print('a - ', len(a))
print()

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
# keys()
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())

# 리스트로 변환
print('a - ', list(a.keys()))
print()

# values()
print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print()

# key와 value 한 번에 같이 - 튜플 형태의 한 쌍으로 구성
print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('a - ', list(a.items()))
print()

# pop() 제거
print('a - ', a.pop('name'))
print('a - ', a)
print()

print('f - ', f.popitem())  # 아무거나 제거
print('f - ', f)
print()

# in 연산자
print('a - ', 'birth' in a)
print('a - ', 'birth2' in a)
print()

# 수정 & 추가
a['birth'] = 1989
print('a - ', a)

a['newKey'] = 'newKey'
print('a - ', a)

a.update(birth='19960926')
print('a - ', a)
temp = {'address': 'Busan'}
a.update(temp)
print('a - ', a)
