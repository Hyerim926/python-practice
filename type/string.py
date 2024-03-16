# 문자형

# 문자열 생성
str1 = 'I am Python'
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you'''

print(type(str1), type(str2), type(str3), type(str4))

# 길이 함수
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열 선언과 할당
str1_t1 = ''
str1_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str1_t2), len(str1_t2))
print()

# 이스케이프 문자 \ 사용
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
# I'm boy
print("I'm boy")
print('I\'m boy')

print('a \t b')  # tab
print('a \nb')  # 줄바꿈
print('a \"\" b')  # "

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄바꿈
t_s1 = 'Click \t Start!'
t_s2 = 'New Line \nCheck!'
print(t_s1)
print(t_s2)
print()

# Raw String r''
raw_s1 = r'D:\\Users\\<NAME>\\Desktop\\'
print(raw_s1)
print()

# 멀티라인 입력 - 역슬래시 사용
multi_str = \
    '''
    I am Python
    I am Python
    I am Python
    I am Python
    '''
print(multi_str)
print()

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "Banana"
str_o4 = "kiwi|banana|apple"

print(str_o1 * 3)  # 문자열이 세 번 반복해서 출력
print(str_o1 + str_o2)

# in과 not in
print('y' in str_o1)  # 문자열도 시퀀스 자료형이기 때문에 가능
print('z' in str_o1)
print('P' not in str_o2)
print()

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

# 문자열 함수
# upper, isalnum, startswith, count, endswith, isalpha
print('Capitalize: ', str_o1.capitalize())
print('endswith: ', str_o2.endswith('e'))
print('replace: ', str_o1.replace('thon', 'good'))
print('sorted: ', sorted(str_o1))  # list 형태로 반환해줌
print('split: ', str_o4.split('|'))

# 반복(시퀀스)
im_str = 'Good Boy!'
print(dir(im_str))  # __iter__
print()

# 출력
for i in im_str:
    print(i)
print()

# 슬라이싱
str_sl = 'Nice Python'

print(len(str_sl))
# 슬라이싱 연습
print(str_sl[0:3]) # 0부터 세 개의 요소만 출력
print(str_sl[5:]) # 5부터 마지막까지
print(str_sl[:len(str_sl)])
print(str_sl[1:4:2]) # 1부터 4개를 가져오는데 2개씩 skip하면서
print(str_sl[-2:]) # 끝에서부터 진행
print(str_sl[1:-2])
print(str_sl[::2]) # 처음부터 끝까지 2개 간격으로 출력
print(str_sl[::-1]) # reverse 처리됨

# 아스키 코드
a = 'z'

print(ord(a)) # 문자 => 아스키 코드
print(chr(122)) # 아스키 코드 => 문자

