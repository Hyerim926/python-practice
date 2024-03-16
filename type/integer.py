# 숫자형

# 파이썬 지원 자료형
"""
int: 정수
float: 실수
complex: 복소수
bool: 불린
str: 문자열(시퀀스) * 시퀀스? 반복문으로 처리할 수 있음
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 사전
"""

# 데이터 타입
str1 = 'Python'
bool = True
str2 = 'Anaconda'
float_v = 10.0  # 10 !== 10.0
int_v = 7
list = [str1, str2]
dict = {
    'name': "Machine Learning",
    'version': 2.0
}
tuple = (7, 8, 9)
tuple = 7, 8, 9
set = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

print()

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x): 절대값
pow(x, y) : x의 y제곱
"""

# 정수 선언
i = 77
i2 = -14
big_int = 77777777777777777777777777777778888888888888888

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산
i1 = 39
i2 = 939
big_int1 = 77777777777777777777779898392895398240
big_int2 = 939824012321052357234091935724023
f1 = 1.234
f2 = 3.939

# +
print('>>>>>+')
print('i1 + i2 :', i1 + i2)
print('f1 + f2 :', f1 + f2)
print('big_int1 + big_int2 :', big_int1 + big_int2)
print()

# *
print('>>>>>*')
print('i1 * i2 :', i1 * i2)
print('f1 * f2 :', f1 * f2)
print('big_int1 * big_int2 :', big_int1 * big_int2)
print()

# 형 변환
a = 3. # 3.0
b = 6  # 얘만 정수
c = .7 # 0.7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))
print()

print(float(a))
print(int(c))
print(int(d))
print(int(True)) # True: 1, False: 0
print(float(False)) # 0.0
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형 -> 복소수
print(complex(False))
print()

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8) # 몫과 나머지를 할당
print(x, y)
print(pow(5, 3), 5 ** 3)
print()

# 외부 모듈 math
import math
print(math.pi)
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수 [올림]