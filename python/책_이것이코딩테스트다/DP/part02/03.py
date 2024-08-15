# 03. 개미 전사
# dp

n = int(input())
storage = list(map(int,input().split()))
dp = [0]*n



for i in range(n):
    if i == 0:
        dp[0] = storage[0]
    elif i == 1:
        dp[1] = max(storage[0],storage[1])
    else:
        dp[i] = max(dp[i-1], dp[i-2]+storage[i])
                
print(dp[-1])     