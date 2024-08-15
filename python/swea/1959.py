

T = int(input())


for t in range(T):
    n,m = map(int,input().split())
    maxNum = 0

    if n > m:
        big = n
        small = m
        b = list(map(int,input().split()))
        a = list(map(int,input().split()))
    else:
        big = m
        small = n
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))

    for i in range(big-small+1):
        calNum = 0
        for j in range(small):
            calNum += a[j]*b[i+j]

        maxNum = max(maxNum,calNum)

    print(f'#{t} {maxNum}')    













