num = list(map(int,input().split()))
best = 1
zz = []
hh = []

for i in range(3):
    if num[i] % 2 == 0:
        zz.append(num[i])
    else:
        hh.append(num[i])
    
if len(hh) > 0:
    for i in range(len(hh)):
        best *= hh[i]
else: 
    for i in range(len(zz)):
        best *= zz[i]

print(best)

    
  for i in range(len(string)):
        if(i % (count+1) ==0):
            print(i,end="")