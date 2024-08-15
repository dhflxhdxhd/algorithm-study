n,m = map(int,input().split())
not_d = [input() for i in range(n)]
not_b = [input() for i in range(m)]

name = list(set(not_d) & set(not_b))
name.sort()

print(len(name))
for n in name:
    print(n)