#골드바흐의 추측
#유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
n=10001
prime = [False,False] + [True]*(n-1)

for i in range(2,int(pow(n,0.5)+1)):
  if prime[i]:
    for j in range(i+i, n+1, i):
        prime[j] = False

# print(prime)

t = int(input())

for i in range(t):
    n = int(input())
    a = n // 2
    b = n // 2
    while True:
        if prime[a] and prime[b]:
            print(a,b)
            break
        else:
            a -= 1
            b += 1