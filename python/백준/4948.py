#베르트랑 공준
#임의의 자연수 n에 대하여 n보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재한다.
import sys
import math
def isPrime(num):
    if num==1:
        return False
    else:
        for k in range(2,int(math.sqrt(num))+1):
            if num%k == 0:
                return False
        return True

#여러 값에 대해 각각의 결과 출력 방법
# 1)
# while True:
#     cnt = 0
#     n =  int(input())
#     if n==0:
#         break
    
#     for i in range(n+1,2*n+1):
#         if isPrime(i):
#             cnt += 1
            
#     print(cnt)

# 2)
for num in sys.stdin:
    cnt=0
    num = int(num)
    if num == 0:
        break
    
    for i in range(num+1,2*num+1):
        if isPrime(i):
            cnt += 1
            
    print(cnt)