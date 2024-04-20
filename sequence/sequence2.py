# 시퀀스형 Sequence : 순서가 있는 데이터
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100, 9))
# print(divmod((100, 9))) # TypeError: divmod expected 2 arguments, got 1
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)  # ValueError: too many values to unpack (expected 3)
print(x, y, rest)  # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
x, y, *rest = range(2)
print(x, y, rest)  # 0 1 []
# x, y, *rest = range(1)
# print(x, y, rest)  # ValueError: not enough values to unpack (expected at least 2, got 1)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)  # 1 2 [3, 4, 5]

print()
print()

# Mutable(가변) vs Immutable(불변)
# tuple은 id값이 매번 바뀌고 list는 바뀌지 않는다
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2  # 재할당해서 Id값이 다름
m = m * 2

print(l, id(l))
print(m, id(m))  # 4340053440

l *= 2
m *= 2

print(l, id(l))
print(m, id(m))  # 4340053440

print()
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환 (원본 수정 x)
f = ['orange', 'apple', 'banana', 'cherry', 'lemon', 'strawberry', 'coconut']
print(f'sorted - {sorted(f)}')
print(f'sorted - {sorted(f, reverse=True)}')  # 역순으로 정렬
print(f'sorted - {sorted(f, key=len)}')  # 각 원소의 길이를 기준으로 정렬
print(f'sorted - {sorted(f, key=lambda x: x[-1])}')  # 마지막 문자를 기준으로 정렬
print(f'sorted - {sorted(f, key=lambda x: x[-1], reverse=True)}')  # 마지막 문자를 기준으로 역순으로 정렬

print(f'before sorted - {f}')

print()
print()

# sort : 정렬 후 객체 직접 변경 (원본 수정)
# 반환 값 확인(None) // None이 js의 Undefined와 유사한 개념
print('sort - ', f.sort(), f)
print('sort - ', f.sort(reverse=True), f)
print('sort - ', f.sort(key=len), f)
print('sort - ', f.sort(key=lambda x: x[-1]), f)
print('sort - ', f.sort(key=lambda x: x[-1], reverse=True), f)

print()
print()

# List vs Array 적합한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환) Array 사용
