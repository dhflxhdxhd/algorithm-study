# 각 행의 가장 작은 수 중 가장 큰 값

n,m = map(int,input().split())

result = 0
for i in range(n):
    data = map(int,input().split())
    value = min(data)
    result = max(result,value)

print(result)
    
