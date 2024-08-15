# 만들 수 없는 금액
# 1. 만들 수 있는 모든 조합 구하기 -> itertools의 combinations(조합) 사용
# 2. 정렬
# 3. 만들지 못한 최소값 구하기
from itertools import combinations
n = int(input())
coins = list(map(int,input().split())) 
cost = []

for i in range(1,len(coins)+1):
    group = list(combinations(coins,i))

    for g in group:
        if sum(g) not in cost:
            cost.append(sum(g))

cost.sort()

for i in range(1,len(cost)+1):
    if i not in cost:
        print(i)
        break

