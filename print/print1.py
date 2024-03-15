# Print 사용법1
# /python3_formatted_output.php

# 기본 출력
print('Python Start!')
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# seperator 옵션 (js의 Array.join()과 유사)
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '7777', sep='-')
print('python', 'gmail.com', sep='@')

print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

# file 옵션
import sys

print('Learn Python', file=sys.stdout)

print()

# format 사용 (d, s, f)
# d: digit 정수
# s: string 문자열
# f: float 소수
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two')) # 순서 지정도 가능

print()

# %s
# 앞에 숫자는 자리수 (js의 String.padEnd() 혹은 js의 String.padStart()와 유사)
# 양수일 땐 왼쪽을 공백으로
print('%10s' % 'nice')
print('{:>10}'.format('nice')) # 왼쪽으로 10자리 확보하고 포맷팅

# 음수일 땐 오른쪽을 공백으로
print('%-10s' % 'nice')
print('{:<10}'.format('nice')) # 오른쪽으로 10자리 확보하고 포맷팅

# 부등호 옆에 있는 문자로 공백 채우기
print('{:_>10}'.format('nice')) # 왼쪽으로 남은 자리를 _로 채우기

# 중앙 정렬
print('{:^10}'.format('nice'))

# 절삭 (js의 String.substring()과 유사)
print('%.5s' % ('nice'))
print('%.5s' % ('pyhtonstudy'))
print('{:10.5}'.format('pythonstudy'))

print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))

print('%-4d' % (42))
print('{:<4d}'.format(42))

print()

# %f
print('%1.8f' % 2.1414141414) # 정수부분은 한자리, 소수부분은 8자리까지
print('{:1.8f}'.format(2.1414141414))

print('%06.2f' % 2.1414141414) # 총 길이는 6이고 남은 정수 부분은 0으로 채운다
print('{:06.2f}'.format(2.1414141414))
