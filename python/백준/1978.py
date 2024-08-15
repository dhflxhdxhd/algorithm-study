#소수찾기
n = int(input())
nums = list(map(int, input().split()))
cnt = 0

def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    
    for i in range(2, num):
        if num % i ==0 :
            return False
    return True

for num in nums :
    if prime(num):
        cnt += 1
print(cnt)
