str = input()
ans = set()
for i in range(len(str)):
    for j in range(i,len(str)):
        t = str[i:j+1]
        ans.add(t)

print(len(ans))