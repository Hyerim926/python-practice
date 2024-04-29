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


# next Pattern
class WordSpliter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % self._text


wi = WordSpliter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()
print()


# Generator Pattern
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word  # 제네레이터, yield가 인덱스 정보를 가지고 있음
        return

    def __repr__(self):
        return 'WordSplitGenerator(%s)' % self._text


wg = WordSplitGenerator('Do today what you could do tomorrow')

wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))
