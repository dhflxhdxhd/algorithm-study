# 1206. 1일차 - View

for t in range(1, 11):
    test = t
    n = int(input())
    listNum = list(map(int, input().split()))

    count = 0
    for l in range(len(listNum)):
        if listNum[l] == 0:
            continue

        target = listNum[l]
        max_b = 0

        if l < 2:
            start = l+1
            end = l+3

        elif l > n-3:
            start = l-2
            end = l

        else:
            start = l-2
            end = l+3

        for i in range(start, end):
            # 자기 자신은 넘어가기
            if i == l:
                continue

            # 만약 target의 크기가 옆에 있는 건물보다 작으면
            if target < listNum[i]:
                check = False
                break
            else:
                check = True
                max_b = max(list[i], max_b)

        if check == True:
            count += (target - max_b)

    print("#%d %d" % (test, count))
