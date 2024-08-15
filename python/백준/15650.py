N,M = map(int,input().split())
arr = []

def BT(st):
    if len(arr) == M:
        print(' '.join(map(str,arr)))
        return

    for i in range(st, N+1):
        if i not in arr: #이미 선택한 숫자를 다시 선택하려 하면 배제하는 방식
            arr.append(i)
            BT(st+1)
            arr.pop()

BT(1)