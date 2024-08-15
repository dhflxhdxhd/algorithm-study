m = int(input())
mums = list(map(int,input().split()))
n = int(input())
nums = list(map(int,input().split()))
count = 0
# for num in nums:
#     for mum in mums:
#         if num == mum:
#             count += 1
#     print(count,end=' ')
#     count = 0

dict = dict()

for mum in mums:
    if mum in dict:
        dict[mum] += 1
    else:
        dict[mum] = 1


for num in nums:
    if num in dict:
        print(dict[num],end=' ')
    else:
        print(0,end=' ')