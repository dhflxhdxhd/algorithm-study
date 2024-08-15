n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

amax = -1e9
amin = 1e9

def result(num,idx, add,sub,mul,div):
    global amax,amin
    if idx == n: #모든 숫자를 탐색했다면
        amax = max(amax,num)
        amin = min(amin,num)
        return

    if add > 0:
        result(num + nums[idx],idx + 1,add-1, sub,mul,div)
    if sub > 0:
        result(num - nums[idx],idx + 1, add, sub -1, mul, div)
    if mul > 0:
        result(num*nums[idx],idx + 1, add,sub,mul -1,div)
    if div > 0:
        result(int(num/nums[idx]),idx + 1, add, sub, mul, div-1)

result(nums[0],1,op[0], op[1], op[2], op[3])
print(amax)
print(amin)