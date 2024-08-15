# 10816 숫자 카드 2

# 이진탐색 이용
# 시간초과
n = int(input())
nums = list(map(int,input().split()))
m = int(input())
mums = list(map(int,input().split()))

nums.sort()
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end) // 2

        if array[mid] == target:
            return array[start:end+1].count(target)
            
        elif array[mid] < target :
            start = mid + 1
        else:
            end = mid - 1
            
    return None


for mum in mums:
    start = 0
    end = len(nums)-1
    result = binary_search(nums,mum,start,end)
    if result is None:
        print(0,end=" ")
    else:
        print(result,end=" ")
