# 일급 함수(일급 객체)
# 클로저 기초

# 파이썬 변수 범위(scope)

# Ex1
def func_v1(a):
    print(a)
    print(b)


# func_v1(10)

# Ex2
b = 20


def func_v2(a):
    print(a)
    print(b)


func_v2(10)

# Ex3
c = 30


def func_v3(a):
    global c # global로 사용된 변수를 로컬 area에서 사용하는 것은 디버깅이 쉽지 않은 코드이므로 지양한다
    # c = 40
    print(a)
    print(
        c)  # UnboundLocalError: cannot access local variable 'c' where it is not associated with a value / global 키워드로 인해 30이 호출됨
    # c = 40  # 로컬 변수가 뒤늦게 선언돼서 사용 불가
    c = 40


print('>>', c)  # 처음 c를 찾을 때는 함수 실행 전이기 때문에 30으로 선언한 전역변수가 호출된다
func_v3(10)
print('>>', c)  # 함수가 실행된 후에 호출되는 c는 함수 내에서 global로 선언한 값인 40이 호출된다

print()
print()

# Closure : 상태를 기억한다
# Closure(클로저) 사용 이유
# 서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock)
# 메모리를 공유하지 않고 메시지 전달로 처리하기 위한 -> Erlang
# 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 구조를 적극적으로 사용 -> 함수형 프로그래밍과 깊은 연관관계
# 클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점

a = 100

print(a + 100)
print(a + 1000)

# 결과 누적(함수 사용)
print(sum(range(1, 51)))
print(sum(range(51, 101)))

print()
print()


# 클래스 이용 / 많이 사용됨
class Averager():
    def __init__(self):
        self._series = [] # 상태를 계속 가지고 있는다

    def __call__(self, v):
        self._series.append(v)
        print(f'inner >> {self._series} / {len(self._series)}')
        return sum(self._series) / len(self._series)


# 인스턴스 생성
averager_cls = Averager()

# 누적
print(averager_cls(10))  # class를 function처럼 실행한다
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(70))
print(averager_cls(193))
