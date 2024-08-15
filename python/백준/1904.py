#1904 

import sys
n = int(sys.stdin.readline())
d = [0] * 1000001
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2])%15746

print(d[n])

def countNum(n):
    if n == 1:
        return 1 ;
    elif n == 2 :
        return 2;

    if d[n] != 0:
        return d[n];

    d[n] = countNum(n-1) + countNum(n-2)
    return d[n]

print(countNum(n) % 15746)
        


error (재귀에러)
# import sys
# n = int(sys.stdin.readline())
# d = [0] * 1000001
# def countNum(n):
#     if n == 1 or n == 2:
#         return n

#     if d[n] != 0 :
#         return d[n]
    
#     d[n] = countNum(n-1) + countNum(n-2)
#     return d[n]

# print(countNum(n)%15746)