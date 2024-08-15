#택시 기하학
#유클리드 기하학

import math
r = int(input())

#유클리드기하학
w = r*r*math.pi
#택시기하학
tw = r*r*2

#{인덱스:0개수.자리수f}.format(숫자)
print("{:.6f}\n{:.6f}".format(w,tw))


