# Print 사용법2
# 파이썬 세 가지 Print Formatting

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

### 3가지 Format Practice
x = 50
y = 100
text = 20240315
n = 'Hwang'

# 출력1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, x + y)
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=x + y)
print(ex2)

# 출력3 - 가장 많이 사용
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)

# 구분기호
m = 10000000
print(f'm: {m:,}')

print()

# 정렬
# ^ : 가운데 정렬
# < : 왼쪽 정렬
# > : 오른쪽 정렬

t = 20

print(f't = {t:10}')  # 일반
print(f't = {t:^10}') # 가운데 정렬
print(f't = {t:>10}') # 오른쪽 정렬
print(f't = {t:<10}') # 왼쪽 정렬

print()

print(f't = {t:*^10}') # 가운데 정렬 & 자리수를 *로 채운다
print(f't = {t:*<10}') # 왼쪽 정렬 & 자리수를 *로 채운다
