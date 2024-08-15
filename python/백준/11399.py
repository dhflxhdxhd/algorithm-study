n = int(input())
idx = [str(i+1) for i in range(n)]
p = list(map(int, input().split()))

dictionary = dict(zip(idx,p))

sorted_dict = sorted(dictionary.items(), key=lambda x : x[1])
sum = 0
result = 0
for i in range(n):
    sum += sorted_dict[i][1]
    result += sum

print(result)

# simple

# n = int(input())
# p = list(map(int, input().split()))
# sum,result = 0,0

# p.sort()

# for i in range(n):
#     sum += p[i]
#     result += sum

# print(result)
