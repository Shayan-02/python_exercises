# Read input values
n, i = map(int, input().split())
array = list(map(int, input().split()))

# Insertion sort algorithm
for step in range(1, n):
    key = array[step]
    j = step - 1

    # Move elements of array[0..step-1], that are greater than key,
    # to one position ahead of their current position
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key

    # Print the array after the i-th step
    if step == i:
        print(' '.join(map(str, array)))
        break