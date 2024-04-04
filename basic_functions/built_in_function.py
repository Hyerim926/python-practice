# 내장함수
# 자주 사용하는 함수 위주로 실습
# str(), int(), tuple() 형변환 이미 학습
# 내장함수라 이미 인터프리터가 가지고 있기 때문에 import를 따로 하지 않음

# abs() : 절대값
print(abs(-3))

# all(), any() : iterable 요소 검사(참, 거짓)
print(all([1, 2, 3]))  # and
print(all([1, 2, 0]))  # False (0)
print(all([1, 2, '']))  # False (빈 문자열)

print(any([1, 2, 0]))  # or / True

# chr() : 아스키 -> 문자, ord() : 문자 -> 아스키
print(chr(67))
print(ord('C'))

# enumerate() : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'def', 'ghi']):
    print(i, name)  # 0 abc


# filter(def, list) : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2


print(list(filter(conv_pos, [1, -3, 0, 2, -5])))

# 람다식 활용
print(list(filter(lambda x: abs(x) > 2, [1, -3, 0, 2, -5])))

# id() : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))

# Len() : 요소의 길이 반환
print(len('abcdefg'))
print(len([1, 2, 3, 4, 5, 6, 7]))

# max(), min() : 최대값, 최소값
print(max([1, 2, 3, 6]))
print(max(['python study']))
print(min([1, 2, 3, 6]))
print(min(['python study']))


# map() : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)


print(list(map(conv_abs, [1, -3, 0, 2, -5])))  # 모든 값들이 절대값으로 반환
print(list(map(lambda x: abs(x), [1, -3, 0, 2, -5])))  # 모든 값들이 절대값으로 반환

# pow() : 제곱값 반환
print(pow(2, 10))

# range() : 반복가능한 객체 반환(Iterable) 반환
print(list(range(1, 10, 2)))  # 홀수만
print(list(range(2, 10, 2)))  # 짝수만
print(list(range(0, -15, -1)))

# round() : 반올림
print(round(5.1324, 2))  # 둘째자리까지만 표현
print(round(5.6))  # 자릿수 지정 안하면 그냥 첫째자리에서 반올림
print(round(5.5454))

# sorted() : 반복가능한 객체(Iterable)를 정렬 후 반환
print(sorted([5, 6, 3, 2, 1]))
a = sorted([5, 6, 3, 2, 1])
print(a)

print(sorted(['p', 'y', 't', 'h', 'o', 'n']))

# sum() : 반복가능한 객체(Iterable) 합 반환
print(sum([3, 5, 2, 6, 1]))
print(sum(range(1, 100)))  # range가 list 반환해서 sum 구하기 가능

# type() : 자료형 확인
print(type(3))
print(type({3, 4}))
print(type(()))
print(type([]))
print(type('sys'))

# zip() : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10, 20, 30], [40, 50, 60])))  # [(10, 40), (20, 50), (30, 60)] / 하나의 리스트를 튜플로 구성
print(list(zip([10, 20, 30], [40, 50])))  # [(10, 40), (20, 50)] / 짝이 없는 것은 제외
print(type(list(zip([10, 20, 30], [40, 50]))[0]))
