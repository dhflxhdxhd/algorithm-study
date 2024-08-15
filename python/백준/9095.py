# 1,2,3 더하기

t = int(input())
for _ in range(t):
    n = int(input())

    def dp(n):
        count = [0]*12
        count[1] = 1
        count[2] = 2
        count[3] = 4

        for i in range(4,n+1):
            # count[i] = count[i-1] + count[i-2] + count[i-3]
            count[i] = sum(count[i-3:i])
        return count[n]

    print(dp(n))