# 14225. 부분수열의 합

from itertools import combinations
import copy
n = int(input())
nums = list(map(int,input().split(" ")))
sNums = copy.deepcopy(nums)

for i in range(2,len(nums)+1):
    combi = list(combinations(nums,i))
    for c in combi:
        sNums.append(sum(c))

sNums.sort()
sNums = list(set(sNums))
target = 1


for i in range(0,len(sNums)):
    if target != sNums[i] :
        print(target)
        break
    elif i == len(sNums)-1:
        print(sNums[i] +1)
        break

    target += 1

    
    