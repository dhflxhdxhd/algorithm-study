# 소수판별
import math
a,b = map(int,input().split())

def isPrime(num):
    if(num == 1): return False
    else:
        for k in range(2,int(math.sqrt(num))+1):
            if num % k == 0:
                return False
        return True

for i in range(a,b+1):
    if isPrime(i):
        print(i)