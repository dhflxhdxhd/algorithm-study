#1654 랜선 자르기

k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
start = 1
end = max(arr)

while start <= end : 
    count = 0 #랜선 개수, m보다 커야함 
    mid = (start+end) // 2

    for a in arr:
        count += a // mid
        
    if count >= n:
        start = mid + 1
    else : 
        end = mid - 1

print(end)