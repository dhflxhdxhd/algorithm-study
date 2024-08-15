#에라토스테네스의 체
#범위에서 합성수를 지우는 방식으로 소수를 찾는 방법. 
    
import math
m,n = map(int,input().split())

def isPrime(num):
    if num == 1:
        return False
    else: 
        for j in range(2,int(math.sqrt(num))+1):
            if num % j == 0:
                return False
        return True
               
                
for i in range(m,n+1):
    if isPrime(i):
        print(i)