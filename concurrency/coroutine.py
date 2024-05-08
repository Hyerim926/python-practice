# 코루틴(Coroutine)
# 코루틴 : 단일(싱글) 스레드, 스택을 기반으로 동작하는 비동기 작업
# 스레드 : OS에서 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티스레드
# yield send : 메인 <-> 서브
# 코루틴 제어, 상태, 양방향 전송

# 서브루틴 : 메인루틴 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로그래밍
# 코루틴 : 스레드에 비해 오버헤드 감소
# 스레드 : 싱글스레드 -> 멀티스레드 -> 복잡 -> 공유되는 자원 -> 데드락/교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가
# def -> async , yield -> await를 사용함

# 코루틴 Ex1
def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine received : {}'.format(i))


# 메인 루틴
# 제네레이터 선언1
cr1 = coroutine1()

print(cr1, type(cr1))


# yield 지점까지 서브루틴 수행
# next(cr1)

# 기본 전달 값 None
# next(cr1)

# 값 전송
# cr1.send(100)  # 메인 루틴과 서브 루틴이 서로 데이터를 교환함 >>> coroutine received : 100

# 잘못된 사용
# cr2 = coroutine1()


# next() 호출하지 않고 send()로 데이터를 보내면 에러 발생
# cr2.send(100)  # TypeError: can't send non-None value to a just-started generator


# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : Yield 대기 상태 -> **중요**
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(x))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))  # GEN_CREATED
print(next(cr3))
print(getgeneratorstate(cr3))  # GEN_SUSPENDED

cr3.send(100)
# print(cr3.send(100))
print()
print()


# 코루틴 Ex3
# StopIteration 자동 처리(3.5+ -> await 처리 가능)
# 중첩 코루틴 처리
def generator1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))  # StopIteration

t2 = generator1()

print(list(t2))  # ['A', 'B', 1, 2, 3]

print()
print()


# for문으로 구현한 것과 동일함
def generator2():
    yield from 'AB'
    yield from range(1, 4)


t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t1))  # StopIteration
