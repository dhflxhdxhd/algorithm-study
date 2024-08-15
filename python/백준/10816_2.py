# 10816 숫자 카드 2
n = int(input())
nums = list(map(int,input().split()))
m = int(input())
mums = list(map(int,input().split()))

dict = dict()

for num in nums:
    # dictionary에서 키의 유무를 확인하기 위함 : in
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

for mum in mums:
    if mum in dict:
        print(dict[mum], end=" ")
    else:
        print(0, end= " ")
