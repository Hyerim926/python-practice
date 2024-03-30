# 모듈
# import {모듈} 형식으로 사용
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일

# 사칙 연산
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x ** y


# print('-' * 15)
# print('called! inner!')
# print(add(5, 5))
# print(subtract(15, 5))
# print(multiply(10, 2))
# print(divide(10, 2))
# print(power(3, 3))
# print('-' * 15)


# __name__ 사용
# 실행하는 위치가 나 자신이라면 이 블록이 실행됨
if __name__ == '__main__':
    print('-' * 15)
    print('called! inner!')
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(10, 2))
    print(divide(10, 2))
    print(power(3, 3))
    print('-' * 15)
