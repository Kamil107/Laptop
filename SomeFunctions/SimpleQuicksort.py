def QuickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        higher = [i for i in array[1:] if i > pivot]
        lower = [i for i in array[1:] if i < pivot]
        return QuickSort(lower) + [pivot] + QuickSort(higher)

print(QuickSort([5, 2, 3, 8, 5, 9, 0]))