def generate_combinations(word):
    # вспомогательная функция для рекурсивной генерации комбинаций
    def generate_combinations_recursive(current_combination, remaining_letters):
        if len(remaining_letters) == 0:
            # базовый случай: если не осталось букв, добавляем текущую комбинацию в список
            combinations.append(current_combination)
        else:
            # рекурсивно генерируем комбинации, добавляя каждую оставшуюся букву к текущей комбинации
            for i in range(len(remaining_letters)):
                new_combination = current_combination + remaining_letters[i]
                new_remaining = remaining_letters[:i] + remaining_letters[i+1:]
                generate_combinations_recursive(new_combination, new_remaining)

    # список для хранения всех комбинаций
    combinations = []
    # начинаем рекурсивный процесс с пустой комбинации и всеми буквами слова
    generate_combinations_recursive("", word)
    return combinations

# пример использования:
word = input("Введите слово: ")
print("Все возможные комбинации букв в слове '{}':".format(word))
combinations = generate_combinations(word)
for combination in combinations:
    print(combination)
