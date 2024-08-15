
# 방법 1
t = int(input())
for _ in range(t):
    test = int(input())
    nums = list(map(int,input().split()))
    d_nums = dict()
    
    for num in nums:
        if  num in d_nums:
            d_nums[num] += 1
        else:
            d_nums[num] = 1
    
    c_max = max(d_nums.values())
    
    print("#", end="")
    print(test, next(key for key, value in d_nums.items() if value == c_max))

# 방법 2
# from collections import Counter

# t = int(input())
# for _ in range(t):
#     test = int(input())
#     nums = list(map(int,input().split()))

#     counter = dict(Counter(nums))
#     count = sorted(counter.items(), key= lambda item:(item[1], item[0]))

#     print("#%d %d"%(test,count[-1][0]))

# 방법 3
# from collections import Counter

# t = int(input())
# for _ in range(t):
#     test = int(input())
#     nums = list(map(int,input().split()))

#     mode = Counter(nums).most_common(3)[0][0]
#     print("#%d %d" %(test,mode))