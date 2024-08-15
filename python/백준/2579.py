# 2579. 계단 오르기
# DP

n = int(input())
stairs = []
dp = [0]*n

for _ in range(n):
    stairs.append(int(input()))

if n <= 2:
    dp[0] = stairs[0]
    dp[1] = sum(stairs)

else:
    dp[0] = stairs[0]
    dp[1] = sum(stairs[0:2])

    for i in range(2,n):
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

print(dp[n-1])        