def insertionSort(array):
    n = len(array)
    for j in range (1 , n):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i]> key:
            array[i + 1] = array[i]
            i -= 1

        array[i+1] = key
    return array

def merge(left , right):
    i = j = 0
    result = list()
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

            
            
def mergeSort( array ):
    if len( array ) > 1:
        left = mergeSort(array[:len( array ) // 2])
        right = mergeSort(array[len( array ) // 2:])
        return merge(left, right)
    return array



if __name__=='__main__':
    print("Enter the numbers to sort:")
    inparray = list(map(int, input().split()))
    print("Sorted array using insertion sort is:", insertionSort(inparray))
    print("Sorted array using merge sort is:", mergeSort(inparray))
    
