#완전탐색
#소수 찾기
import itertools
import math

def isPrime(num):
    if(num == 1): return False
    else:
        for k in range(2,int(math.sqrt(num))+1):
            if num % k == 0:
                return False
        return True

def solution(numbers):
    num = [n for num in numbers]
    print(num)
    print(num)


soltion(17)