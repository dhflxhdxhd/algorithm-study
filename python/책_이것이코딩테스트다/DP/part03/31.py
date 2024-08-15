# Q.31 금광 

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    size = [[] for _ in range(m)]


    for i in range(len(array)):
        for j in range(m):
            if i % m == j:
                size[j].append(array[i])    

    dp = size[:]

    for i in range(1,m):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + size[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + size[i][1]
        dp[i][2] = max(dp[i-1][1], dp[i-1][2]) + size[i][2]

    print(max(dp[-1]))
