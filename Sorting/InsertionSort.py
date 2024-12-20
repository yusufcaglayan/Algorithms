numbers = [33,44,21,83,56,73,22]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    while j >= 0 and key < numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key
   
print("Sıralanmış Liste:", numbers)
