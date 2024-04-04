# 외장함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shuffle, temfile, time, random등

# 예제 1
import sys

print(sys.argv)

# 예제 2(강제 종료)
# sys.exit()

# 예제 3(파이썬 패키지 위치)
print(sys.path)

# pickle : 객체 파일 쓰기, 파이썬에서 읽을 수 있는 데이터 타입(class, list, dict, tuple 등)을 파일로 사용할 수 있다
import pickle

# 예제 4(쓰기)
f = open('test.obj', 'wb')
obj = {
    1: 'python',
    2: 'study',
    3: 'basic'
}
pickle.dump(obj, f)  # 해당 경로에 파일이 쓰여짐
f.close()

# 예제 5(읽기)
f = open('test.obj', 'rb')
data = pickle.load(f)
print(data, type(data))
f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir, rmdir(비어 있으면 삭제), rename

# 예제 6
import os

print(os.environ)
print(os.environ["PATH"])

# 예제 7(현재 경로)
print(os.getcwd())

# time : 시간 관련 처리
import time

# 예제 8
print(time.time())  # 1712237694.666392 숫자 형식으로 프린트

# 예제 9(형태 변환)
print(time.localtime(time.time()))

# 예제 10(간단 표현)
print(time.ctime())  # Thu Apr  4 22:35:47 2024

# 예제 11(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 예제 12(시간 간격 발생)
for i in range(5):
    print(i)
    # 1초 마다 for문을 실행
    # time.sleep(1)  # 이렇게 쓰는 경우 많지 않음 js의 setTimeOut()과 유사

# random : 난수 리턴
import random

# 예제 13
print(random.random())  # 0 ~ 1 실수 js의 Math.random()

# 예제 14
print(random.randint(1, 45))  # 1 - 45
print(random.randrange(1, 45))  # 1 - 44

# 예제 15(섞기)
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)

# 예제 16(무작위 선택)
c = random.choice(d)  # 1~5중에 랜덤으로 선택
print(c)

# webbrowser : 본인 OS의 웹 브라우저 실행
import webbrowser

webbrowser.open('https://www.youtube.com/watch?v=')
webbrowser.open_new('https://www.youtube.com/watch?v=')  # 새 탭으로 열기
