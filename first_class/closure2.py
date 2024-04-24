# 클로저 심화
# 클로저 : 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능

# Closure 사용
def closure_ex1():
    # Free variable
    # 클로저 영역
    series = []

    def averager(v):
        series.append(v)
        print(f'inner >>> {series} / {len(series)}')
        return sum(series) / len(series)

    return averager


avg_closure1 = closure_ex1()

print(avg_closure1)  # <function closure_ex1.<locals>.averager at 0x1027228e0>

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()

# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))  # co_* / co_freevars (클로저)
print(avg_closure1.__code__.co_freevars)  # ('series',)
print(avg_closure1.__closure__[0].cell_contents)  # [10, 30, 50] / free 변수에 대한 값

print()
print()


# 잘못된 클로저 사용 예
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):  # cannot access local variable 'cnt' where it is not associated with a value
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_ex2()


# print(avg_closure2(10))

# 수정된 예 (nonlocal) 사용
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total  # nonlocal로 선언한다
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_ex3()
print(avg_closure3(15))
print(avg_closure3(45))
print(avg_closure3(60))
