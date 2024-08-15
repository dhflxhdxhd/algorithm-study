n = int(input())
nums = list(map(int,input().split(" ")))
m = int(input())
mums = list(map(int,input().split(" ")))

nums.sort()

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return 1
        elif nums[mid] > target:
            end = mid-1
        else:
            start = mid+1
        
    return 0

for mum in mums:
    start = 0
    end = len(nums) - 1
    print(binary_search(nums,mum,start, end))

