# 11055. 가장 큰 증가하는 부분 수열
# dp
# import copy
n = int(input())
nums = list(map(int,input().split()))

# dp[i] : nums[i]로 끝나는 합이 가장 큰 증가하는 부분 수열의 합
# dp = copy.deepcopy(nums)
dp = nums[:]

target = 0
for i in range(1,n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+nums[i])

print(max(dp))
