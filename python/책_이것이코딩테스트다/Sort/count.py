# 계수정렬 count sort

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array) + 1)

# 0부터 count 리스트가 만들어졌음.
for i in range(len(array)):
    count[array[i]] += 1

# len(count) 출력
for i in range(len(count)):
    # index값을 count만큼 출력
    for j in range(count[i]):
        print(i , end=" ")
