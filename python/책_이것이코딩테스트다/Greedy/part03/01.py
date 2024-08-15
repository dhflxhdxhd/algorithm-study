#모험가길드
n = int(input())
fears = list(map(int,input().split()))
fears.sort()

count = 0
# group = []
result = 0

for fear in fears:
    # group.append(fear)
    count += 1 #그룹에 해당 모험가 추가
    if count >= fear:
        # print(group)
        group = []
        count = 0
        result += 1

print(result)