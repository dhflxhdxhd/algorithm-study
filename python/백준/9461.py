# 9461. 파도반수열

# 방법 1
t = int(input())

d = [0] * 101
d[1],d[2],d[3] = 1, 1, 1
d[4],d[5] = 2, 2

def showP(n):
    for i in range(6, n+1):
        d[i] = d[i-1] + d[i-5]

    return d[n]

for i in range(t):
    n = int(input())
    print(showP(n))


# 방법 2
t = int(input())
d = [0] * 101

def showP(n):
    if n == 1:
        return 1
        
    if n >= 2 and n <= 5:
        return n // 2

    if d[n] != 0:
        return d[n]

    d[n] = showP(n-1) + showP(n-5)
    return d[n]

for i in range(t):
    n = int(input())
    print(showP(n))