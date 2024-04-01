# 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할된 개별적인 모듈로 구성
# __init__.py : Python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성을 추천한다, 안그러면 import가 되지 않음 / 약간 js에서 export의 느낌
# 상대경로 : ..(부모 디렉토리), .(현재 디렉토리) -> 모듈 내부에서만 사용

# 예제 1 (같은 경로에 있는 패키지)
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제 2
# js ver: import * from sub.sub2
from sub.sub1 import module1
from sub.sub2 import module2 as m2  # alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()
print()

# 예제 3
from sub.sub1 import *  # 모든 메서드를 가지고 오는 방법, 하지만 지양하자
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()
module2.mod2_test1()
module2.mod2_test2()

print()
print()
print()

# 연습
from sub.sub3 import calculate as cal

print(cal.add(3, 4))
print(cal.power(2, 3))
print(cal.multiply(4, 10))
print(cal.divide(6, 3))
print(cal.subtract(10, 9))
