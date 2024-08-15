n = int(input())

arr = []
for i in range(n):
    arr.append(input().split())

arr.sort(key=lambda score : (-int(score[1]), int(score[2]), -int(score[3]), score[0]) )

for a in arr:
    print(a[0])