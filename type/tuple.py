# 튜플
# 리스트와 비교
# 특징 : 순서 o, 중복 o, 수정 x, 삭제 x)
# 불변 : immutable

# 선언
a = ()
b = (1)  # 이렇게 하면 타입이 int가 됨
c = (1,)  # 이렇게 해야 타입이 tuple이 됨
d = (11, 12, 13, 14)
e = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

# 인덱싱
print('>>>>> indexing')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', list(e[-1][1]))  # tuple to list
print()

# 수정 불가
# d[0] = 1500 # Tuples don't support item assignment

# 슬라이싱
print('>>>>> slicing')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3])
print()

# 연산
print('>>>>> calculate')
print('c + d', c + d)
print('c * 3', c * 3)
print()

# 함수
a = (1, 2, 3, 4, 5)
print('>>>>> def')
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))
print()

# 팩킹과 언팩킹(Packing and Unpacking)
print('>>>>> Packing and Unpacking')
# 팩킹
t = ('foo', 'bar', 'baz', 'qux')
# 언팩킹1 - js의 구조분해할당과 비슷하다
(x1, x2, x3, x4) = t  # 괄호가 없어도 동작은 하지만 컨벤션은 괄호가 있는 것
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹
t2 = 1, 2, 3  # 괄호가 없어도 튜플 선언
t3 = 4,

# 언팩킹
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
