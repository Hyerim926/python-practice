# 예외 처리

# 예제 1 -> 예외처리
try:
    n = int(input('Enter a number: '))
    print('Ok. Your number is {}'.format(n))
except ValueError:
    print('This is not a number')

print()

# 예제 2 -> 올바른 값 입력 완료까지 지속
while True:
    try:
        n = int(input('Enter a number: '))
        break
    except ValueError:
        print('This is not a number')
print('Ok. Your number is {}'.format(n))