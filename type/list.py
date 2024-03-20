# 리스트
# 자료구조에서 중요
# 배열을 대체해서 사용 가능
# 리스트 자료형
# 순서, 중복, 수정, 삭제가 모두 가능

# 선언
a = []
b = list()
c = [70, 75, 80, 85]  # len()
print(len(c))
print()
# 서로 다른 자료형 담기
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [212.33425, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>> indexing')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])  # 오른쪽에서 첫번째 요소
print('e - ', e[-1][1])  # Base
print('e - ', list(e[-1][1]))  # to list
print()

# 슬라이싱
print('>>>>> slicing')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])
print()

# 리스트 연산 - 리스트 + 리스트 = 리스트 (js의 spread연산자로 더하는 것과 유사)
print('>>>>> calculate')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))  # int => str로 형변환해서 더해주기
print()

# 값 비교
print('>>>>> compare')
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
print('>>>>> identity')
temp = c
print(temp, c)
print(id(temp), id(c))  # 동일한 주소값
print()

# 리스트 수정, 삭제
print('>>>>> update, delete')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']  # [['a', 'b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []  # 삭제 메커니즘과 비슷
print('c - ', c)
del c[2]  # 삭제
print('c - ', c)
print()

# 리스트 함수
print('>>>>> def')
a = [5, 2, 3, 1, 4]
print('a - ', a)
# a[5] = 10 # 이렇게는 불가

# append : 마지막에 삽입
print('append')
a.append(10)
print('a - ', a)
print()

# sort : 정렬
print('sort')
a.sort()
print('a - ', a)
print()

# reverse : 역순으로
print('reverse')
a.reverse()
print('a - ', a)
print()

# index : 인덱스 함수
print('index')
print('a - ', a.index(3))
print()

# insert : 원하는 위치에 값을 삽입
print('insert')
a.insert(2, 7)
print('a - ', a)
a.reverse()
print('a - ', a)
print()

# remove : 원하는 요소를 제거
print('remove')
a.remove(10)
print('a - ', a)
print()

# pop : 마지막 요소를 제거하고 그 요소를 반환
print('pop')
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print()

# count : 찾는 요소의 개수
print('count')
print('a - ', a.count(4))
print()

# ex : 배열 덧붙이기
print('ex')
ex = [8, 9]
a.extend(ex)
print('a - ', a)
print()

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)

print('a - ', a)
