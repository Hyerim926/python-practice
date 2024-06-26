# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Interator), 함수(Functions), 클래스(Class)

# Magic Method 란
# 클래스 안에 정의할 수 있는 특별한(Built-in) 메소드

# 클래스 예제2
# 벡터(x,y) : 좌표 데이터
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10

class Vector(object):
    def __init__(self, *args):
        """
        Create a vector, example : v = Vector(5, 10)
        """
        if len(args) == 0:
            self.__x, self.__y = 0, 0
        else:
            self.__x, self.__y = args

    def __repr__(self):
        """
        Return the vector information
        """
        return f'Vector({self.__x}, {self.__y})'

    def __add__(self, other):
        """
        Return the vector addition of self and other
        """
        return Vector(self.__x + other.__x, self.__y + other.__y)

    def __mul__(self, y):
        """
        Return the vector multiple of self and other
        """
        return Vector(self.__x * y, self.__y * y)

    def __bool__(self):
        """
        Return if the vector is (0,0)
        """
        return bool(max(self.__x, self.__y))


# Vector 인스턴스 생성
v1 = Vector(5, 1)
v2 = Vector(23, 35)
v3 = Vector()

# 매직메소드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)

print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))
