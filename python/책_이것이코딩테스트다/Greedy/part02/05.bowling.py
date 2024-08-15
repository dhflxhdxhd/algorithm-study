# 볼링공 고르기

from itertools import combinations

n,m = map(int,input().split())
k = list(map(int,input().split()))
count = 0

bowling_combi = list(combinations(k,2))

for combi in bowling_combi:
    if combi[0] != combi[1]:
        count += 1

print(count)