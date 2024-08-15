#bisect 라이브러리

from bisect import bisect_left, bisect_right

# a = [1,2,4,4,8]
# target = 4

# print(bisect_left(a,target)) # output : 2
# print(bisect_right(a,target)) # output : 4

def count_by_range(a,left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)

    return right_index - left_index

a = [1,2,4,4,8]

print(count_by_range(a,4,4))