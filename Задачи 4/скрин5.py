import csv


def sum_column(csv_file, column_index):
    total_sum = 0
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                value = float(row[column_index])
                total_sum += value
            except ValueError:
                # пропускаем неправильные значения
                pass
    return total_sum

# пример
csv_file = 'data.csv'
column_index = 3  # (нумерация с 0)

try:
    total = sum_column(csv_file, column_index)
    print(f"Сумма числовых значений в столбце {column_index}: {total}")
except FileNotFoundError:
    print("Файл не найден.")
except IndexError:
    print("Указан неверный индекс столбца.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
