#잃어버린 괄호
#그리디
#level2

str = input().split("-")
ans = []
for s in str:
    result = 0
    nums = s.split("+")
    for num in nums:
        result += int(num)
    ans.append(result)

answer = ans[0]
# ans.pop(0)

# for a in ans:
#     answer -= a

# print(answer)

for i in range(1,len(ans)):
    answer -= ans[i]
print(answer)

    

