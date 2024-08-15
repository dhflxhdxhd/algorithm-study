# 1912. 연속합

n = int(input())
nums = list(map(int,input().split()))
d = [0] * n
d[0] = nums[0]  # 초기 설정 : 0번째 숫자를 넣음

for i in range(1, len(nums)):
    d[i] = max(nums[i], d[i-1] + nums[i]) 

print(max(d))

