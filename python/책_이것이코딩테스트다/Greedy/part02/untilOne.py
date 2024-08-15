# n과 k 입력받기
n,k = map(int,input().split())
count = 0

# 첫번째 조건) N은 K보다 항상 크거나 같다
while n >= k:
  # 만일 나눠지지 않는다면 1번(1빼기) 실행
  if(n%k != 0): 
    n -= 1
    count += 1
  # k로 나누기
  n = n//k 
  count += 1

# 나머지 수가 1이 될 때까지 빼기 
while n>1:
  n -= 1
  count += 1

print(count)

