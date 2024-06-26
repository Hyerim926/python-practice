# 행맨 미니 게임 제작(2)
# 프로그램 완성 및 최종 테스트

import time
# csv 처리
import csv
# 랜덤
import random

# 사운드 처리
from pygame import mixer
from pygame.mixer import music

mixer.init()

# 처음 인사
name = input('Please enter your name: ')

print('Hello ' + name + '! Time to play Hangman Game!')

print()

time.sleep(1)

print('Start Loading...')
print()
time.sleep(0.5)

# CSV 단어 리스트 선언
words = []

# 문제 CSV 파일 로드
with open('../resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    # Header Skip
    next(reader)

    for row in reader:
        words.append(row)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words)  # ['wagon', 'type of vehicle']

# 정답 단어
word = q[0].strip()  # strip() 공백제거

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 횟수
    failed = 0

    # 정답 단어 반복
    for letter in word:
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if letter in guesses:
            # 추측 단어 출력
            print(letter, end=' ')
        else:
            # 틀린 경우 대시로 처리
            print('_', end=' ')
            failed += 1

    # 단어 추측이 성공한 경우
    if failed == 0:
        print()
        print()
        # 성공 사운드
        music.load('../sound/good.wav')
        music.play()
        time.sleep(1)
        # 성공 메시지
        print('You won! The word was: ', word)
        # while 구문 중단
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    # 힌트
    print('Hint : {}'.format(q[1].strip()))
    guess = input('Guess a letter: ')

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -= 1

        # 오류 메시지
        print('Oops! Wrong letter, try again.')
        # 남은 기회 출력
        print('You have ' + str(turns) + ' more guesses left.')

        if turns == 0:
            # 실패 사운드
            music.load('../sound/bad.wav')
            music.play()
            time.sleep(1)
            # 실패 메시지
            print('You lost! The word was: ', word)
