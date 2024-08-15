n = int(input()) # 거슬러줘야 할 돈
count = 0

# 그리디 알고리즘
# 정당성) 가지고 있는 동전 중 큰 단위가 항상 작은 단위의 배수이므로.
# 큰 단위부터
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin  # 거슬러 줄 수 있는 동전의 개수
    n %= coin # 거슬러 주고 남은 돈n
    
print(count)
