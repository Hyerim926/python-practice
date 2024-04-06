# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, 테스트 모드 : t, 바이너리 모드 b
# 기본값은 t
# 상대 경로('../, ./'), 절대 경로('/Users/hwanghyerim/Library..')

# 파일 읽기(Read)
# 예제1

f = open('../resource/it_news.txt', 'r', encoding='utf-8')

# 속성 확인
print(dir(f))

# 인코딩 확인
print(f.encoding)

# 파일 이름
print(f.name)

# 모드 확인
print(f.mode)  # 현재 모드: read

# 텍스트 확인
cts = f.read()
print(cts)

# 반드시 close
f.close()

print()

# 예제 2
# with : 한 프로세스를 매번 열고 닫고 할 필요가 없음, 가독성 향상
with open('../resource/it_news.txt', 'r', encoding='utf-8') as f:
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제 3
# read() : 전체 읽기, read(10) : 10Byte 읽기

with open('../resource/it_news.txt', 'r', encoding='utf-8') as f:
    c = f.read(20)
    print(c)
    print(len(c))
    c = f.read(20)  # 마지막에 어디까지 읽는지 기억하고서 처리됨, 커서
    print(c)
    f.seek(0, 0)  # 다시 처음부터
    c = f.read(20)
    print(c)

print()

# 예제 4
# readline() : 한 줄 씩 읽기
with open('../resource/it_news.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)

print()

# 예제 5
# readlines : 전체를 읽은 후 라인 단위로 리스트로 저장
with open('../resource/it_news.txt', 'r', encoding='utf-8') as f:
    cts = f.readlines()
    print(cts)
    print()
    for line in cts:
        print(line, end='')

print()

with open('../resource/it_news.txt', 'r', encoding='utf-8') as f:
    line = f.read()
    print(line.split('\n'))

# 파일 쓰기(write)
# 예제 1
with open('../resource/contents1.txt', 'w') as f:
    f.write('I love Python\n')

# 예제 2 append
with open('../resource/contents1.txt', 'at') as f:
    f.write('I love Python2\n')

# 예제 3
# writelines : 리스트 -> 파일
with open('../resource/contents2.txt', 'w') as f:
    list = ['Apple\n', 'Banana\n', 'Cherry\n', 'Melon\n']
    f.writelines(list)

# 예제 4
with open('../resource/contents3.txt', 'w') as f:
    print('Test Text Write!', file=f)  # console에 출력되지 않고 파일에 작성됨
    print('Test Text Write!', file=f)
    print('Test Text Write!', file=f)
