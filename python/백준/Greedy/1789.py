# 1789. 수들의 합

n = int(input())
sum = 0

for i in range(1,n+1):
    sum += i

    if sum > n:
        result = i-1
        break 

print(result)
