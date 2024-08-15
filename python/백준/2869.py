import math

a,b,v = map(int, input().split())
day = 0

day = (v-b) / (a-b)
print(math.ceil(day))
        