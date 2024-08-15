n,k = map(int,input().split())
list = []
for i in range(1,n):
    if n%i==0:
        list.append(i)
    
list.append(n)
if len(list) < k:
    print(0)
else:
    print(list[k-1])