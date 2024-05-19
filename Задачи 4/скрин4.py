def longest_nonincreasing_subsequence(nums):
    # инициализируем массивы для длин и предшественников
    length = [1] * len(nums)
    predecessor = [-1] * len(nums)

    # для каждого элемента в списке
    for i in range(1, len(nums)):
        # проходим по всем предыдущим элементам
        for j in range(i):
            # если предыдущий элемент не меньше текущего
            if nums[j] >= nums[i]:
                # обновляем длину и предшественника
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    predecessor[i] = j

    # находим индекс последнего элемента наибольшей невозрастающей последовательности
    max_length_index = 0
    for i in range(1, len(length)):
        if length[i] > length[max_length_index]:
            max_length_index = i

    # восстанавливаем последовательность
    longest_subsequence = []
    current_index = max_length_index
    while current_index != -1:
        longest_subsequence.append(nums[current_index])
        current_index = predecessor[current_index]

    # переворачиваем последовательность, так как мы начинали с конца
    longest_subsequence.reverse()
    return longest_subsequence

# пример использования
nums = [5, 3, 8, 4, 2, 7, 6, 1]
result = longest_nonincreasing_subsequence(nums)
print("Наибольшая невозрастающая последовательность:", result)
