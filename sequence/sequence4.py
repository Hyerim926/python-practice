# 시퀀스형 Sequence : 순서가 있는 데이터
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 x, Set -> 중복 허용 x
# Dict 및 Set 심화

# immutable Dict / 읽기 전용, 수정 불가
from types import MappingProxyType

d = {'key1': 'value1'}  # 수정 가능

# Read Only
d_frozen = MappingProxyType(d)  # 수정 불가능

# print(d, id(d), hash(d)) # unhashable type: 'dict'
print(d, id(d))  # unhashable type: 'dict'

# print(d_frozen, id(d_frozen), hash(d_frozen)) # unhashable type: 'dict'
print(d_frozen, id(d_frozen))

# 수정 가능
d['key2'] = 'value2'
print(d)

# 수정 불가
# d_frozen['key2'] = 'value2'  # 'mappingproxy' object does not support item assignment

print()
print()

# Set
s1 = {'Apple', 'Orange', 'Banana', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Banana', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
# s4 = {}  # 원소가 없을 때는 Dict로 선언됨
s4 = set()
s5 = frozenset({'Apple', 'Orange', 'Banana', 'Apple', 'Orange', 'Kiwi'})

# 추가 가능
s1.add('Melon')
print(s1)

# 추가 불가
# s5.add('Melon')  # 'frozenset' object has no attribute 'add'

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

print()
print()

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
# dis 모듈 : 바이트 코드가 어떻게 생성되는지 순서 확인 가능
from dis import dis

# {}와 set() 속도 차이 - {}가 더 빠름
print('------')
print(dis('{10}'))  # LOAD_CONST -> BUILD_SET -> RETURN_VALUE [3단계로 실행됨]
print('------')
print(dis('set([10])'))  # PUSH_NULL -> LOAD_NAME -> LOAD_CONST -> BUILD_LIST -> CALL -> RETURN_VALUE [5단계로 실행됨]

print()
print()

# 지능형 집합(Comprehending Set)
print('------')

from unicodedata import name

print({name(chr(i), '') for i in range(0, 256)})
