# 32. 정수 삼각형

size = int(input())
tri = []

for _ in range(size):
    tri.append(list(map(int,input().split())))


dp = tri[:]

for i in range(1,size):
    dp[i][0] = dp[i-1][0] + tri[i][0]
    dp[i][i] = dp[i-1][i-1] + tri[i][i]
    
    if i == 1:
        continue

    for j in range(i-1):
        dp[i][j+1] = max(dp[i-1][j], dp[i-1][j+1]) + tri[i][j+1]
    

print(max(dp[-1]))
    
        
 