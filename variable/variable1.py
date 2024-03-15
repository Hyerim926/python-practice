# 변수

# 기본 선언
n = 700

print(n)
# 타입을 출력
print(type(n))

print()

# 동시선언
x = y = z = 700
print(x, y, z)

print()

# 선언과 재선언
var = 75
var = 'Change Value'
print(var)
print(type(var))

print()

# Object References
# 변수 값 할당 과정
# 1. 타입에 맞는 오브젝트를 생성한다
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

print()

# 예2)
# n -> 777
n = 777
print(n, type(n))
print()

m = n
print(n, m)
print(type(n), type(m))
print()

m = 400
print(m, type(m))
print()

# id, 객체의 고유값 확인
# 두 변수의 고유값이 서로 다름
m = 800
n = 655
print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 값이 똑같으면 고유값도 동일함 (파이썬 내부에서 중복된 코드의 비효율을 인식하여 그렇게 동작함
m = 800
n = 800
print(id(m))
print(id(n))
print(id(m) == id(n)) # true

# 다양한 변수 선언
# Camel Case : numberOfLanguages -> Method 선언 시
# Pascal Case : NumberOfLanguages -> Class 선언 시
# Snake Case : number_of_languages -> Variable 선언 시

# 허용하는 변수 선언법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능
"""
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""