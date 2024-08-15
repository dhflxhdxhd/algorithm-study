#카드 정렬하기
#가장 작은 크기의 두 카드 묶음을 꺼내서 합치고 다시 삽입.
#우선순위 큐 -> heap 이용
import heapq
n =  int(input())

h = []
for _ in range(n):
    heapq.heappush(h,int(input()))

result = 0
while len(h) != 1:
    #가장 작은 크기의 두 카드 꺼냄.
    one = heapq.heappop(h)
    two = heapq.heappop(h)
    #두 카드 합
    sum_value = one + two
    #최종 결과 값에 더함
    result += sum_value
    #두 카드 합 다시 heap에 push
    heapq.heappush(h,sum_value)

print(result)