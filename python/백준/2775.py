# 부녀회장이 될테야
# apt
# 1 6 21 56 126
# 1 5 15 35 70
# 1 4 10 20 35
# 1 3 6 10 15
# 1 2 3 4 5 

t = int(input())

for _ in range(t):  
    k = int(input()) # k층
    n = int(input()) # n호
    apt = [i for i in range(1, n+1)] #apt 초기화
    # print(apt)
    
    for _ in range(k):
        for x in range(1,n):
            apt[x] += apt[x-1]
        # print(apt)
    print(apt[-1]) #apt 가장 마지막 수
   