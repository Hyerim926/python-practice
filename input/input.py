# 사용자 입력
# Input 사용법
# 기본 타입은 str

# 예제 1
name = input('Enter your name')
grade = input('Enter your grade')
company = input('Enter your company')

print(name, grade, company)

print()

# 예제 2
number = input('Enter number : ')
name = input('Enter name')

print('type of number', type(number))
print('type of name', type(name))
print('number * 3', number * 3)

print()

# 예제 3 (계산)
first_number = int(input('Enter number1 : '))
second_number = int(input('Enter number2 : '))

total = first_number + second_number
print('first_number + second_number is ', total)

print()

# 예제 4
float_number = float(input('Enter a float number : '))

print('input float : ', float_number)
print('input type : ', type(float_number))

print()

# 예제 5
print("FirstName = {0}, LastName = {1}".format(input('Enter first name '), input('Enter second name ')))