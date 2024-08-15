array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 종료조건 : 부분리스트들이 더이상 분할이 불가능할 때 종료. > 리스트의 크기가 0이나 1이 될 때 종료.
    if start >= end:
        return

    pivot = start #pivot 설정
    left = start + 1
    right = end

    # left가 right보다 작을 동안 반복
    while left <= right:
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
    
        # left와 right 위치가 엇갈린다면
        if left > right:
            # pivot과 right의 위치를 바꿔라.
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # left와 right의 위치를 바꿔라.
            array[right], array[left] = array[left], array[right]
        
    #순환적 호출(재귀)
    quick_sort(array,start,right-1) #왼쪽 배열 퀵정렬
    quick_sort(array, left, end) # 오른쪽 배열 퀵 정렬 (left = right+1)
    
quick_sort(array,0,len(array)-1)
print(array)    
        
