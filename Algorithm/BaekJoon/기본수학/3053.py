# 택시 기하학

import math

radius = int(input())

# 유클리드 원의 넓이
print(f"{math.pi * radius * radius:.6f}")
# 택시 기하학 원의 넓이
print(f"{2 * radius * radius:.6f}") # 마름모의 넓이 = 2r * 2r * 1/2
