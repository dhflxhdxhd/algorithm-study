from bisect import bisect_left, bisect_right

n = int(input())
nums = list(map(int,input().split()))
m = int(input())
mums = list(map(int,input().split()))

def count_by_range(array,target):
    right_index = bisect_right(array,target)
    left_index = bisect_left(array,target)
    return right_index - left_index


nums.sort()
for mum in mums:
    result = count_by_range(nums,mum)
    if result:
        print(result, end=" ")
    else:
        print(0, end= " ")
    