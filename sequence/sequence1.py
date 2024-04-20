# 시퀀스형 Sequence : 순서가 있는 데이터
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&^%$#@!'  # 불변형, 플랫
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# Comprehending Lists (Recommend)
code_list2 = [ord(s) for s in chars]  # 속도가 좀 더 우세
print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))

# 전체출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)

print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()

# Generator 생성
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지x)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(type(tuple_g))  # <class 'generator'>
print(next(tuple_g))  # next()로 값 하나씩 반환
print(type(array_g))  # <class 'array.array'>
print(array_g.tolist())  # array => list

print()
print()

# 제네레이터 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))
for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

print()
print()

# 리스트 주의
marks1 = [['~'] * 3 for _ in range(4)]  # 사용하지 않은 원소는 _로 선언 가능
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
# [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
print(marks2)
# [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']] / 하나의 주소값이 복사되어 len이 4인 list로 생성되었기 때문

# 증명
print([id(i) for i in marks1])  # [4308697216, 4308630912, 4308629760, 4307841664]
print([id(i) for i in marks2])  # [4308703296, 4308703296, 4308703296, 4308703296]
