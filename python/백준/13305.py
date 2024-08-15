
n = int(input())
km = list(map(int, input().split()))
cost = list(map(int,input().split()))
result = 0
standard_cost = cost[0]

for i in range(n-1):
    if standard_cost > cost[i]:
        standard_cost = cost[i]
    result += standard_cost * km[i]

print(result)

# 부분성공
# min_cost = min(cost[:-1])
# sum,result,rest = 0, 0, 0

# for idx,now_cost in enumerate(cost):
#     if now_cost == min_cost:
#         for i in km[idx:]:
#             rest += i
#         result += now_cost * rest
#         break
#     else:
#         sum = now_cost * km[idx]
#         result += sum

# print(result)