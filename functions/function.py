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
