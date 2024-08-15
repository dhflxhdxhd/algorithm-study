array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    # pivot을 기준으로 pivot보다 작거나 같은 값을 왼쪽, pivot보다 큰 값을 오른쪽.
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # print(left_side)
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))