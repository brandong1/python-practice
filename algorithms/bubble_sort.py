# Bubble Sort
# Time complexity = O(n^2), quadratic
# Space complexity = 0(1)

def bubble_sort(arr):
    '''Bubble sort consists of making multiple passes through a list, comparing elements one by one, and swapping adjacent items that are out of order.'''
    swap_happened = True
    while swap_happened:
        print('bubble sort status: ' + str(arr))
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]

l = [6,8,1,4,10,7,8,9,3,2,5]
bubble_sort(l)

# bubble sort status: [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
# bubble sort status: [6, 1, 4, 8, 7, 8, 9, 3, 2, 5, 10]
# bubble sort status: [1, 4, 6, 7, 8, 8, 3, 2, 5, 9, 10]
# bubble sort status: [1, 4, 6, 7, 8, 3, 2, 5, 8, 9, 10]
# bubble sort status: [1, 4, 6, 7, 3, 2, 5, 8, 8, 9, 10]
# bubble sort status: [1, 4, 6, 3, 2, 5, 7, 8, 8, 9, 10]
# bubble sort status: [1, 4, 3, 2, 5, 6, 7, 8, 8, 9, 10]
# bubble sort status: [1, 3, 2, 4, 5, 6, 7, 8, 8, 9, 10]
# bubble sort status: [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]