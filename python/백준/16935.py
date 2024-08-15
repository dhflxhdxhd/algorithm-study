# 16935. 배열 돌리기3
# 구현

n,m,method = map(int,input().split())
arr = []

# arr 초기화
for i in range(n):
    arr.append(list(map(int,input().split())))


# 상하 반전
def method1(array):
    newArr = []
    for i in range(n,0,-1):
        newArr.append(array[i-1])

    return newArr

# 좌우 반전
def method2(array):
    
    for i in range(n):
        for j in range(m,0,-1):
            newArr[i].append(array[i][j-1])

    return newArr

# 오른쪽 90도 회전
def method3(array):
    newArr = [[] for _ in range(m)]

    for j in range(m):
        for i in range(n,0,-1):
            newArr[j].append(array[i-1][j])

    return newArr

# 왼쪽 90도 회전
def method4(array):
    newArr = [[] for _ in range(m)]

    for j in range(m,0,-1):
        for i in range(n):
            newArr[m-j].append(array[i][j-1])

    return newArr


def method4(array):


    return newArr

newArr = method4(arr)


# 출력
for a in newArr:
    print(*a, sep=" ")
