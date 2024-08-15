#에라토스테네스의 체
#범위에서 합성수를 지우는 방식으로 소수를 찾는 방법. 

#소수구하기
n = 1000
a = [False,False] + [True]*(n-1)  #0~1000 
# print(len(a)) 1001개
primes = []

for i in range(2,n+1):
    if a[i]: #a[i]가 True이면
        primes.append(i)
    for j in range(2*i,n+1 , i): #i의 배수를 False로 설정.
        a[j] = False

print(primes)
