numbers = [5, 7, 2, 9, 6, 1, 3, 8]

# Selection Sort Algorithm
for i in range(len(numbers)):  # Iterate over the list
    min = i  # Assume the current index holds the minimum value
    
    # Find the index of the smallest element in the remaining list
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min]:
            min = j
    
    # Swap the found minimum element with the current element
    # Swapping (2 kabı yer değiştirmek için 1 kap daha lazım)
    temp = numbers[i]
    numbers[i] = numbers[min]
    numbers[min] = temp


print("Sorted list:", numbers)
