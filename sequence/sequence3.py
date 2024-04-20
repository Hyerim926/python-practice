# 시퀀스형 Sequence : 순서가 있는 데이터
# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 해시 테이블 Hashtable
# Key에 Value를 저장하는 구조
# 파이썬 dict 해시 테이블
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조 O(1)
# Key 값을 해싱 함수 -> 해시 주소 -> key에 대한 value 참조

# 참고 : 파이썬 엔진은 해시 테이블로 구성되어있다
# Dict 구조
print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))  # tuple은 해시 주소 존재하여 직접 접근 가능
# print(hash(t2))  # unhashable type: 'list' / list는 immutable하기 때문에 해시 주소값 생성 불가

print()
print()

# Dict setdefault 예제
source = (
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
    ('k2', 'val5'),
)

# key가 중복되면 새로운 값으로 덮어씌워짐
print(dict(source))  # {'k1': 'val2', 'k2': 'val5'}

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)  # {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}

# Use Setdefault (Recommend)
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의사항 - comprehending way는 setdefault 방식으로 사용 불가
new_dict3 = {k: v for k, v in source}
print(new_dict3)  # {'k1': 'val2', 'k2': 'val5'}
