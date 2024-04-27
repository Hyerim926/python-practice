# 병행성(Concurrency)
# 이터레이터, 제너레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text, list, Dict, Set, Tuple, unpacking, *args... : Iterable

t = 'ABCDEFGHIJKLMNOPQRSTUVZ'

print(dir(t))  # __iter__

# 반복 가능한 이유 : 내부적으로 iter() 함수 호출
for c in t:
    pass
    print('>', c)

print()
print()

# 실행 프로세스 / 동작 원리
# while
w = iter(t)

print(dir(w))  # __iter__, __next__
print(next(w))  # A
print(next(w))  # B
print(next(w))  # C

print()
print()

while True:
    try:
        print(next(w))
    except StopIteration:
        break

print()

# 반복형 확인
from collections import abc

print(hasattr(t, '__iter__'))  # True
print(isinstance(t, abc.Iterable))  # True
