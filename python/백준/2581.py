#소수
m = int(input())
n = int(input())
primes = []

for num in range(m,n+1):
    cnt = 0
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                cnt += 1
                break
        if cnt == 0:
            primes.append(num)

if len(primes)>0:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)