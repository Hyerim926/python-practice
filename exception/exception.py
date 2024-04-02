# 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)에서 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다
# 3. 예외는 던져진다
# 4. 예외 무시

# SyntaxError : 문법 오류
# print('error)
# print('error'))
# if True
#     pass

# NameError : 참조 없음
a = 10
b = 15
# print(c)

# ZeroDivisionError
# print(100 / 0)  # 0으로 나눌 수 없음

# IndexError
x = [50, 70, 90]
print(x[1])
# print(x[4]) # !Error
print(x.pop())
print(x.pop())
print(x.pop())
# print(x.pop())  # 빈 리스트에서 pop() 할 때 에러

# KeyError
dic = {'Name': 'John', 'Age': 11, 'City': 'New York'}
# print(dic['hobby'])  # !Error
print(dic.get('hobby'))

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)
# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time

# print(time.time2())

# ValueError
x = [10, 50, 90]
x.remove(50)
print(x)
# x.remove(200)  # x not in list

# FileNotFoundError
# f = open('test.txt')  # No such file or directory: 'test.txt'

# TypeError : 자료형에 맞지 않는 연산을 수행할 경우
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y)  # TypeError: can only concatenate list (not "tuple") to list
# print(x + z)
# print(y + z)

print(x + list(y))
print(x + list(z))

print()

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 : 여러개 가능
# else : try 블록의 에러가 없을 경우 실행 (for-else 와 유사)
# finally : 항상 마지막에 실행

name = ['Kitty', 'John', 'Smith']

# 예제1
# try:
#     z = 'Kitty'  # Cho -> except 구문 실행
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except ValueError:
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

print()

# 예제 2
# try:
#     z = 'Kitty'  # Cho -> except 구문 실행
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# # except:
# except Exception:  # 모든 에러를 처리함
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

print()

# 예제 3
# try:
#     z = 'Cho'  # Cho -> except 구문 실행
#     x = name.index(z)
#     print('{} Found it! {} in name'.format(z, x + 1))
# except Exception as e:  # alias를 선언해서 에러를 출력할 수 있음
#     print(e)
#     print('Not found it! - Occurred ValueError!')
# else:  # 예외가 발생하지 않아야 실행
#     print('Ok! else.')
# finally:  # 예외가 발생해도 안해도 항상 실행
#     print('Ok! finally!')

print()
# 예제 4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생 throw Error()와 유사
try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! Pass!')
    else:
        raise ValueError
        # raise ValueError('Custom error message')  # customMessage 설정법 -> print(e) 실행됨
except ValueError as e:
    # print(e)
    print('Occurred! Exception!')
else:
    print('Ok! else!')
