# 모듈 사용 실습
import sys

print(sys.path)
print(type(sys.path))  # list

# 모듈 삽입
# sys.path.append('/Users/hwanghyelim/PycharmProjects/test/')

# print(sys.path)

# import test_module

# 모듈 사용
# print(test_module)

import module

print(module.add(5, 3))
