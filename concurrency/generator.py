# 제네레이터 Generator
# 병행성 Concurrency : 한 컴퓨터가 여러 일을 동시에 수행, 마지막에 한 일이 무엇인지 알고 있어야함(closure가 그 역할) -> 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성 Parallelism : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator Ex1
def generator_ex1():
    print('Start')
    yield 'A Point'  # yield가 들어간 함수는 Generator 취급을 받음
    print('Continue')
    yield 'B Point'
    print('End')


temp = iter(generator_ex1())

print(temp)  # <generator object generator_ex1 at 0x10079f040>
print(next(temp))  # Start / A Point
print(next(temp))  # Continue / B Point
# print(next(temp))  # End / Traceback (most recent call last):

for v in generator_ex1():
    print(v)

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp2:
    print(i)

for i in temp3:
    print(i)

# Generator Ex3 (중요 함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby...
import itertools

# 숫자를 무한대로 선언
gen1 = itertools.count(1, 2.5)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

# 조건
gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))

for v in gen2:
    pass
    # print(v)

print()

# 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print(v)

print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    pass
    # print(v)

print()

# 연결1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))

print(list(gen5))

print()

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

print()

# 개별
gen7 = itertools.product('ABCDE')
print(list(gen7))

print()

# 개별
gen8 = itertools.product('ABCDE', repeat=4)
print(list(gen8))

print()

# 그룹화
gen9 = itertools.groupby('AAABBBCCCCCDDEE')
# print(list(gen9))
for chr, group in gen9:
    print(chr, ' : ', list(group))
