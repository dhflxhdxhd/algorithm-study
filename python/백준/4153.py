
while(True):
    num = list(map(int,input().split()))
    if(sum(num) == 0):break
    maxnum = max(num)
    num.remove(maxnum)
    if maxnum**2 == num[0]**2 + num[1]**2: print("right")
    else: print("wrong")