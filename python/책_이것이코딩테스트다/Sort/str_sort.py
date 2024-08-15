# str = ["119", "97674223", "1195524421"]
# str = ["12", "123", "1235", "567", "88"]
# str.sort()
# print(str)
from collections import Counter

p = ["leo","kiki", "eden"]
c = ["eden", "kiki"]
p.sort()
c.sort()

answer = Counter(p) - Counter(c)
print(list(answer)
# def sol(p,c):
#     p.sort()
#     c.sort()
#     for i in range(len(c)):
#         if (p[i] != c[i]):
#             return p[i]

#     return p[-1]

print(p[-1])
# print(p)
# print(c)