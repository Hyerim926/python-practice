# 집합(Set)
# 순서x, 중복x
import sys

# 선언
a = set()
b = set([1, 2, 3])  # set 안에 list 형식으로 할당
c = set([1, 2, 'str'])
d = {'foo', 'bar', 'baz', 'foo', 'qux'}  # key 없이 {} 안에 넣으면 set
e = {42, 'foo', (1, 2, 3), 3.123124}
print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print()

# 튜플 변환(set to tuple)
t = tuple(b)
print('t - ', type(t), t)
# 슬라이싱 가능 - 튜플
print('t - ', t[0], t[1:3])
print()

# 리스트 변환(set to list)
l = list(c)
l2 = list(e)
print('l - ', l)
print('l2 - ', l2)
print()

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print()

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 집합의 교집합
print('>>>>> 집합의 교집합')
print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))
print()

# 집합의 합집합
print('>>>>> 집합의 합집합')
print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))
print()

# 집합의 차집합
print('>>>>> 집합의 차집합')
print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))
print()

# 중복 원소 확인
print('>>>>> 집합의 중복 원소 확인')
print('s1 & s2 : ', s1.isdisjoint(s2))  # 교집합 o : False, 교집합 x : True
print()

# 부분 집합 확인
print('>>>>> 부분 집합 확인')
print('s1은 s2의 부분 집합인가?', s1.issubset(s2))  # s1은 s2의 부분 집합인가?
print('s1은 s2의 상위 집합인가?', s1.issuperset(s2))  # s1은 s2의 상위 집합인가?
print()

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7) # 없는 원소 삭제 시 에러

s1.discard(3)
print('s1 - ', s1)
s1.discard(7)  # 없는 원소 삭제 시 예외 발생 x

# 전부 삭제
# 리스트도 clear 사용 가능
s1.clear()
print('s1 - ', s1)
