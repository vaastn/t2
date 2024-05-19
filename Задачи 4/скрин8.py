import random


# заданный словарь слов
dictionary = ["слово", "кроссворд", "генерация", "решение", "программа", "python", "алгоритм"]

# функция для генерации кроссворда
def generate_crossword(words):
    # создаем пустую сетку
    grid = [[' ' for _ in range(10)] for _ in range(10)]

    # вставляем слова по вертикали или горизонтали
    for word in words:
        direction = random.choice(['вертикально', 'горизонтально'])
        if direction == 'вертикально':
            x = random.randint(0, 9)
            y = random.randint(0, 9 - len(word))
            for i, letter in enumerate(word):
                grid[y + i][x] = letter
        else:
            x = random.randint(0, 9 - len(word))
            y = random.randint(0, 9)
            for i, letter in enumerate(word):
                grid[y][x + i] = letter

    # выводим кроссворд
    for row in grid:
        print(' '.join(row))

# функция для решения кроссворда
def solve_crossword(words, grid):
    # просто выводим слова из словаря
    for word in words:
        print(word)

# генерация кроссворда
print("Сгенерированный кроссворд:")
generate_crossword(dictionary)

# решение кроссворда
print("\nРешение кроссворда:")
solve_crossword(dictionary, None)  # пока что предполагаем, что мы не знаем кроссворд
