#1931
#회의실 배정

n = int(input())
time_list = []

for i in range(n):
    x,y = map(int,input().split())
    time_list.append([x,y])

time_list.sort(key = lambda x : (x[1], x[0]))
print(time_list)
count = 0
end_time = 0

for start, end in time_list:
    if start >= end_time:
        # print([start,end])
        count += 1
        end_time = end 

print(count)