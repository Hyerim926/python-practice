# 일급 함수(일급 객체)
# 함수형 프로그래밍을 가능하도록 해줌 (js도 아래와 같은 성질을 지님)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 함수 객체

def factorial(n):
    """
    Factorial function
    :param n: int
    :return:
    """
    if n == 1:  # n < 2
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))  # <class 'function'> <class 'type'>
print(dir(factorial))  # 함수지만 객체 취급을 한다
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
# 함수만 가지고 있는 성질
# {'__get__', '__annotations__', '__closure__', '__globals__', '__kwdefaults__', '__type_params__',
# '__builtins__', '__call__', '__code__', '__name__', '__qualname__', '__defaults__'}
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial
print(var_func)  # <function factorial at 0x100cbe0c0>
print(var_func(10))
print(map(var_func, range(1, 11)))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce
# js의 es6와 동일

# 값은 모두 동일하다 하지만 comprehending 방법이 더 가독성이 좋다
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])  # 0은 false 취급을 하므로 홀수만 fatcorial 함수로 실행하여 반환

print()
print()

# reduce
from functools import reduce
from operator import add  # 더해주는 함수

print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))  # 속도는 이것이 더 우세

# 익명함수(lambda)
# 가급적 주석을 꼭 작성하자
# 가급적 익명함수보다는 일반함수로 사용하는 것을 권장

print(reduce(lambda x, t: x + t, range(1, 11)))  # add 함수를 익명함수로 사용

print()
print()

# callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str))  # str('a')
print(callable(A))  # class 호출 가능
print(callable(list))
print(callable(var_func))
print(callable(factorial))
print(callable(3.14))  # False

print()
print()

# Partial 사용법 : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5)  # 5 * ? / 함수를 인자로 전달 가능하고 함수를 변수에 할당

# 고정 추가
six = partial(five, 6)  # 5 * 6

print(five(10))
print(five(100))

print(six())  # 실행만 해도 계산가능
print([five(i) for i in range(1, 11)])  # 5의 배수
print(list(map(five, range(1, 11))))
