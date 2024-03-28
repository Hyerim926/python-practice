# 함수

# 파이썬 함수식 및 람다(lamda)

# 함수 정의 방법
# def function_name(parameter):
#     code

# 예제 1
def first_func(name):
    print('Hello,', name)


word = 'Hyerim'
first_func(word)

print()


# 예제 2
def return_func(name):
    value = 'Hello, ' + str(name)
    return value


x = return_func('Hyerim')
print(x)

print()


# 예제 3 (다중반환)
def func_mul1(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3


x, y, z = func_mul1(10)
print(x, y, z)

print()


# 튜플 리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)  # 패킹됨


t = func_mul2(20)
print(t, type(t), list(t))

print()


# 리스트 리턴
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]  # 패킹됨


l = func_mul3(20)
print(l, type(l), set(l))

print()


# 딕셔너리 리턴
def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'k1': y1, 'k2': y2, 'k3': y3}  # 패킹됨


d = func_mul4(2)
print(d, type(d), d.get('k2'), list(d.items()))

print()


# 중요
# *args, **kwargs

# *args(언팩킹)
# 매개변수의 수가 가변적이라는 의미 / 그 매개변수는 튜플형태일 경우에 쓰인다
def args_func(*args):  # 매개변수명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-----')


args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')

print()


# **kwargs 언팩킹
# 딕셔너리 형태일 경우에 쓰인다
def kwargs_func(**kwargs):  # 매개변수명 자유
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('-----')


kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Park')
kwargs_func(name1='Lee', name2='Park', name3='Kim')

print()


# 전체 혼합
def example(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


example(10, 20, 'Lee', 'Kim', 'Park', age1=20, age2=30, age3=40)

print()


# 중첩함수 (클로저)
def nested_func(num):
    def func_in_func(num):
        print(num)

    print('In func')
    func_in_func(num + 100)  # 중첩함수를 여기서 호출, 외부에서 호출 불가


nested_func(100)

print()


# 람다식 예제
# 장점: 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 너무 남발 시에는 가독성이 오히려 감소된다

# 함수식
def mul_func(x, y):
    return x * y

print(mul_func(10, 50))

print()

# 일반적 함수 -> 변수에 할당
mul_func_var = mul_func
print(mul_func_var(20, 50))

print()

# 람다 함수 -> 변수에 할당
# 호출부가 없기 때문에 변수에 담아 사용한다 js의 명명함수와 비슷하다
lambda_mul_func = lambda x, y: x * y
print(lambda_mul_func(50, 50))

print()

# 매개변수에 함수를 넣으려고 할 때
def func_final(x, y, func):
    print('>>>>', x * y * func(100, 100))

func_final(10, 20, lambda x,y: x * y)
func_final(10, 20, mul_func_var)
func_final(10, 20, lambda_mul_func)
