# 이코테
# 숫자 카드 게임
# 가장 작은 수의 모임 중 가장 큰 수
n, m = map(int, input().split())
result = 0

for i in range(n):
    cards = map(int,input().split())
    minCard = min(cards)
    result = max(result,minCard)

print(result);
    
    
