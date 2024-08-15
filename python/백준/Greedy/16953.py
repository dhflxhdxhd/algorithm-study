# 16953. A -> B

start, end = map(int, input().split())
count = 1

while start != end:
    count += 1
    temp = end
    if end % 2 == 0:
        end = end // 2
    elif str(end)[-1] == "1":
        end = end // 10

    # 값의 변화가 없을 때
    if temp == end:
        count = -1
        break

print(count)
